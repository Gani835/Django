from rest_framework import serializers

from.models import Foodsales

class FoodsalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Foodsales
        fields='__all__'