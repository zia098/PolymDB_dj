from django.contrib import admin
from .models import WildTypePolymerase, ModifiedPolymerase, FusionDomain

@admin.register(WildTypePolymerase)
class WildTypePolymeraseAdmin(admin.ModelAdmin):
    list_display = ("name", "source_strain", "family", "exo_activity", "doi")
    search_fields = ("name", "source_strain", "family")

@admin.register(ModifiedPolymerase)
class ModifiedPolymeraseAdmin(admin.ModelAdmin):
    list_display = ("name", "base_polymerase", "modification_type", "optimal_temp", "activity", "doi")
    search_fields = ("name", "base_polymerase", "modifications")

@admin.register(FusionDomain)
class FusionDomainAdmin(admin.ModelAdmin):
    list_display = ("name", "functional_type", "source_protein", "strain", "length", "doi")
    search_fields = ("name", "functional_type", "strain")
