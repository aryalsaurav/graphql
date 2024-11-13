from django.urls import path

from .views import (
    CategoryCreateView,
    ProductCreateView,
    OrderItemCreateView,
    OrderCreateView,
)


app_name = 'e-commerce_v1'

urlpatterns = [
    path('category/',CategoryCreateView.as_view(),name="category-create"),
    path('product/',ProductCreateView.as_view(),name="product-create"),
    path('order-item/',OrderItemCreateView.as_view(),name="order_item-create"),
    path('order/',OrderCreateView.as_view(),name="order-create"),
    
]