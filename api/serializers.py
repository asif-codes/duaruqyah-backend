from rest_framework import serializers
from .models import (Category, SubCategory, Dua)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class DuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dua
        fields = '__all__'