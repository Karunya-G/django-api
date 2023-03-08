from rest_framework import serializers
from .models import *


class AnnoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annote
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagess
        fields = "__all__"