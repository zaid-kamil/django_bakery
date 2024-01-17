from django.urls import path
from . import views
urlpatterns = [
    path('collection/detail/<int:id>', views.collection, name='collection_detail'),
    path('collection/all', views.collection_list, name='collection_all'),
    path('product/<int:id>', views.product, name='product_detail'),
    path('product/all', views.product_list, name='product_all'),
]