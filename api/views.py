from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Category, SubCategory, Dua)
from .serializers import (CategorySerializer, SubCategorySerializer, DuaSerializer)
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.

class CategoryAPIView(APIView):
     def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     
class SubCategoryAPIView(generics.ListAPIView):
    serializer_class = SubCategorySerializer
    
    def get_queryset(self):
        # cat_id = self.kwargs.get('cat_id')

        queryset = SubCategory.objects.all()
        return queryset
    
class DuaAPIView(generics.ListAPIView):
    serializer_class = DuaSerializer
    
    def get_queryset(self):

        queryset = Dua.objects.all()
        return queryset