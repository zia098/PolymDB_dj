# polymes/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
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
    # Fetch and order each queryset
    wild_qs     = WildTypePolymerase.objects.all().order_by('name')
    modified_qs = ModifiedPolymerase.objects.all().order_by('name')
    fusion_qs   = FusionDomain.objects.all().order_by('name')

    # Paginate each: 20 items per page
    wild_paginator     = Paginator(wild_qs, 20)
    modified_paginator = Paginator(modified_qs, 20)
    fusion_paginator   = Paginator(fusion_qs, 20)

    # Get the current page numbers from query params
    wild_page     = request.GET.get('wild_page', 1)
    modified_page = request.GET.get('mod_page', 1)
    fusion_page   = request.GET.get('fusion_page', 1)
    
    # Get the page objects
    wild_page_obj = wild_paginator.get_page(wild_page)
    modified_page_obj = modified_paginator.get_page(modified_page)
    fusion_page_obj = fusion_paginator.get_page(fusion_page)

    context = {
        'wild_types': wild_page_obj,
        'modifieds': modified_page_obj,
        'fusions': fusion_page_obj,
        'wild_page_range': get_page_range(wild_paginator, wild_page_obj),
        'modified_page_range': get_page_range(modified_paginator, modified_page_obj),
        'fusion_page_range': get_page_range(fusion_paginator, fusion_page_obj),
    }
    return render(request, 'polymes/list.html', context)
    
def wildtype_detail(request, pk):
    polymerase = get_object_or_404(WildTypePolymerase, pk=pk)
    return render(request, 'polymes/wildtype_detail.html', {'polymerase': polymerase})

def modified_detail(request, pk):
    polymerase = get_object_or_404(ModifiedPolymerase, pk=pk)
    return render(request, 'polymes/modified_detail.html', {'polymerase': polymerase})

def domain_detail(request, pk):
    domain = get_object_or_404(FusionDomain, pk=pk)
    return render(request, 'polymes/domain_detail.html', {'domain': domain})

# Add this to your views.py file
def get_page_range(paginator, page, window=2):
    """Return a limited page range around the current page."""
    current_page = page.number
    total_pages = paginator.num_pages
    
    # Start with a window around current page
    start = max(current_page - window, 1)
    end = min(current_page + window, total_pages)
    
    # Add first and last pages if they're not already included
    page_range = []
    if start > 1:
        page_range.extend([1])
        if start > 2:
            page_range.extend(['...'])
    
    page_range.extend(range(start, end + 1))
    
    if end < total_pages:
        if end < total_pages - 1:
            page_range.extend(['...'])
        page_range.extend([total_pages])
    
    return page_range
