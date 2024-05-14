from rest_framework import serializers
from API.models import Bike



class Bikeserializer(serializers.ModelSerializer):

    class Meta:
        model=Bike
        fields="__all__"
        read_only_fields=["id"]


