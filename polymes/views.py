# polymes/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import WildTypePolymerase, ModifiedPolymerase, FusionDomain

def polymerase_list(request):
    # fetch & order
    wild_qs     = WildTypePolymerase.objects.all().order_by('name')
    modified_qs = ModifiedPolymerase.objects.all().order_by('name')
    fusion_qs   = FusionDomain.objects.all().order_by('name')

    # paginate (10 per page)
    wild_paginator     = Paginator(wild_qs, 10)
    modified_paginator = Paginator(modified_qs, 10)
    fusion_paginator   = Paginator(fusion_qs, 10)

    # pull page numbers from querystring
    wild_page     = request.GET.get('wild_page')
    modified_page = request.GET.get('mod_page')
    fusion_page   = request.GET.get('fusion_page')

    context = {
        'wild_types': wild_paginator.get_page(wild_page),
        'modifieds' : modified_paginator.get_page(modified_page),
        'fusions'   : fusion_paginator.get_page(fusion_page),
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

