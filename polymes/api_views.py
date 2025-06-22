# polymes/api_views.py
from rest_framework import generics
from .models import ModifiedPolymerase
from .serializers import ModifiedPolymeraseSerializer

class PolymeraseListCreateAPIView(generics.ListCreateAPIView):

    queryset = ModifiedPolymerase.objects.all()
    serializer_class = ModifiedPolymeraseSerializer

class PolymeraseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ModifiedPolymerase.objects.all()
    serializer_class = ModifiedPolymeraseSerializer
