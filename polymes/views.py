from django.shortcuts import render
from .models import WildTypePolymerase, ModifiedPolymerase, FusionDomain
from django.http import JsonResponse



def polymerase_list(request):
    wild_types = WildTypePolymerase.objects.all()
    modifieds = ModifiedPolymerase.objects.all()
    fusions = FusionDomain.objects.all()

    return render(request, 'polymes/list.html', {
        'wild_types': wild_types,
        'modifieds': modifieds,
        'fusions': fusions,
    })
