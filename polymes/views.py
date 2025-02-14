from django.shortcuts import render
from .models import WildTypePolymerase, ModifiedPolymerase, FusionDomain
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404



def polymerase_list(request):
    wild_types = WildTypePolymerase.objects.all()
    modifieds = ModifiedPolymerase.objects.all()
    fusions = FusionDomain.objects.all()

    return render(request, 'polymes/list.html', {
        'wild_types': wild_types,
        'modifieds': modifieds,
        'fusions': fusions,
    })


def wildtype_detail(request, pk):
    polymerase = get_object_or_404(WildTypePolymerase, pk=pk)
    return render(request, 'polymes/wildtype_detail.html', {'polymerase': polymerase})

def modified_detail(request, pk):
    polymerase = get_object_or_404(ModifiedPolymerase, pk=pk)
    return render(request, 'polymes/modified_detail.html', {'polymerase': polymerase})

def domain_detail(request, pk):
    domain = get_object_or_404(FusionDomain, pk=pk)
    return render(request, 'polymes/domain_detail.html', {'domain': domain})
    
