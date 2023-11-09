from django.urls import path
from .views import (CategoryAPIView, SubCategoryAPIView, DuaAPIView)

urlpatterns = [
    path('category/', CategoryAPIView.as_view()),
    path('subcategory/', SubCategoryAPIView.as_view()),
    path('dua/', DuaAPIView.as_view()),
]