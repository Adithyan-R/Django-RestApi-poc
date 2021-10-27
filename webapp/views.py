from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Product

# Create your views here.


class ProductViewSet(ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()