from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,DestroyAPIView
from.models import Foodsales
from.serializers import FoodsalesSerializer
# Create your views here.

class Foodsales(ListAPIView):
    queryset=Foodsales.objects.all()
    serializer_class=FoodsalesSerializer
    