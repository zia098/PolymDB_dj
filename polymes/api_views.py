# polymes/api_views.py
from rest_framework import generics
from .models import ModifiedPolymerase
from .serializers import ModifiedPolymeraseSerializer
from django_filters.rest_framework import DjangoFilterBackend





class PolymeraseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ModifiedPolymerase.objects.all()
    serializer_class = ModifiedPolymeraseSerializer


class PolymeraseListCreateAPIView(generics.ListCreateAPIView):
    queryset = ModifiedPolymerase.objects.all()
    serializer_class = ModifiedPolymeraseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['base_polymerase', 'modification_type', 'optimal_temp']
    search_fields    = ['name', 'modifications']
    ordering_fields  = ['optimal_temp', 'activity']
