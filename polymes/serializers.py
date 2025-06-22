# polymes/serializers.py
from rest_framework import serializers
from .models import ModifiedPolymerase

class ModifiedPolymeraseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModifiedPolymerase
        # 
        fields = '__all__'
