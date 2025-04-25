# polymes/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Case, When, Value, CharField, F
from .models import WildTypePolymerase, ModifiedPolymerase, FusionDomain

def get_page_range(paginator, page, window=2):
    """Return a limited page range like [1, '...', 4,5,6, '...', total]."""
    current = page.number
    total   = paginator.num_pages

    start = max(current - window, 1)
    end   = min(current + window, total)

    rng = []
    if start > 1:
        rng.append(1)
        if start > 2:
            rng.append('...')
    rng.extend(range(start, end+1))
    if end < total:
        if end < total - 1:
            rng.append('...')
        rng.append(total)
    return rng


def polymerase_list(request):
    # Fetch wild type and fusion domain querysets
    wild_qs = WildTypePolymerase.objects.all().order_by('name')
    fusion_qs = FusionDomain.objects.all().order_by('name')
    
    # Annotate modified polymerases with a custom sort field
    # This puts letters first, then numbers, then symbols
# Force names to start with letters to be sorted case-insensitively
    modified_qs = ModifiedPolymerase.objects.all().annotate(
        sort_prefix=Case(
        When(name__regex=r'^[A-Za-z]', then=Value('0')),
        When(name__regex=r'^[0-9]', then=Value('1')),
        default=Value('2'),
        output_field=CharField(),
        )
     ).order_by('sort_prefix', 'name')
    
    # Get search term
    search_term = request.GET.get('search', '')
    
    # Apply search to modified polymerases if search term exists
    if search_term:
        modified_qs = modified_qs.filter(
            Q(name__icontains=search_term) | 
            Q(base_polymerase__icontains=search_term) | 
            Q(modification_type__icontains=search_term)
        )
    
    # Apply filters to modified polymerases
    opt_temp_min = request.GET.get('opt_temp_min')
    opt_temp_max = request.GET.get('opt_temp_max')
    melt_temp_min = request.GET.get('melt_temp_min')
    activity_min = request.GET.get('activity_min')
    base_poly = request.GET.get('base_poly')
    mod_type = request.GET.get('mod_type')
    
    # Filter the modified_qs based on parameters
    if opt_temp_min:
        try:
            modified_qs = modified_qs.filter(optimal_temp__gte=float(opt_temp_min))
        except (ValueError, TypeError):
            # Handle non-numeric values gracefully
            pass
    if opt_temp_max:
        try:
            modified_qs = modified_qs.filter(optimal_temp__lte=float(opt_temp_max))
        except (ValueError, TypeError):
            pass
    if melt_temp_min:
        try:
            modified_qs = modified_qs.filter(melting_temp__gte=float(melt_temp_min))
        except (ValueError, TypeError):
            pass
    if activity_min:
        try:
            modified_qs = modified_qs.filter(activity__gte=float(activity_min))
        except (ValueError, TypeError):
            pass
    if base_poly:
        modified_qs = modified_qs.filter(base_polymerase__icontains=base_poly)
    if mod_type:
        modified_qs = modified_qs.filter(modification_type__icontains=mod_type)
    
    # Paginate each
    wild_paginator = Paginator(wild_qs, 20)
    modified_paginator = Paginator(modified_qs, 20)
    fusion_paginator = Paginator(fusion_qs, 20)

    # Get the current page numbers
    wild_page = request.GET.get('wild_page', 1)
    modified_page = request.GET.get('mod_page', 1)
    fusion_page = request.GET.get('fusion_page', 1)
    
    # Get page objects
    wild_page_obj = wild_paginator.get_page(wild_page)
    modified_page_obj = modified_paginator.get_page(modified_page)
    fusion_page_obj = fusion_paginator.get_page(fusion_page)
    
    # Pass active filter values to template
    filter_params = {
        'opt_temp_min': opt_temp_min or '',
        'opt_temp_max': opt_temp_max or '',
        'melt_temp_min': melt_temp_min or '',
        'activity_min': activity_min or '',
        'base_poly': base_poly or '',
        'mod_type': mod_type or '',
    }
    
    # Create query string for detail page links
    query_params = ''
    if modified_page:
        query_params += f'mod_page={modified_page}'
    if search_term:
        query_params += f'&search={search_term}'
    if opt_temp_min:
        query_params += f'&opt_temp_min={opt_temp_min}'
    if opt_temp_max:
        query_params += f'&opt_temp_max={opt_temp_max}'
    if melt_temp_min:
        query_params += f'&melt_temp_min={melt_temp_min}'
    if activity_min:
        query_params += f'&activity_min={activity_min}'
    if base_poly:
        query_params += f'&base_poly={base_poly}'
    if mod_type:
        query_params += f'&mod_type={mod_type}'

    context = {
        'wild_types': wild_page_obj,
        'modifieds': modified_page_obj,
        'fusions': fusion_page_obj,
        'wild_page_range': get_page_range(wild_paginator, wild_page_obj),
        'modified_page_range': get_page_range(modified_paginator, modified_page_obj),
        'fusion_page_range': get_page_range(fusion_paginator, fusion_page_obj),
        'filter_params': filter_params,
        'query_params': query_params,
        'search_term': search_term,  # Add search term to context
    }
    return render(request, 'polymes/list.html', context)
    
def wildtype_detail(request, pk):
    polymerase = get_object_or_404(WildTypePolymerase, pk=pk)
    
    # Get referrer params
    ref_params = {}
    for key, value in request.GET.items():
        ref_params[key] = value
    
    return render(request, 'polymes/wildtype_detail.html', {
        'polymerase': polymerase,
        'ref_params': ref_params
    })

def modified_detail(request, pk):
    polymerase = get_object_or_404(ModifiedPolymerase, pk=pk)
    
    # Extract referrer parameters
    ref_params = {}
    for key, value in request.GET.items():
        ref_params[key] = value
    
    return render(request, 'polymes/modified_detail.html', {
        'polymerase': polymerase,
        'ref_params': ref_params
    })

def domain_detail(request, pk):
    domain = get_object_or_404(FusionDomain, pk=pk)
    
    # Get referrer params
    ref_params = {}
    for key, value in request.GET.items():
        ref_params[key] = value
    
    return render(request, 'polymes/domain_detail.html', {
        'domain': domain,
        'ref_params': ref_params
    })
