

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ListProduct,ProductDetailview,Cart,ProductCreateView
from .views import CartViewSet

router = DefaultRouter()
router.register('cart',CartViewSet,basename='cart')



urlpatterns = [

    path('product-list',ListProduct.as_view(),name='list'),
    path('product-detail/<int:pk>/',ProductDetailview.as_view(),name='detail'),

    path('product-create/', ProductCreateView.as_view(), name='product_create'),

    path('',include(router.urls)),
    path('cart/<int:pk>/list_cart_items/',CartViewSet.as_view({'get':'list_cart_items'}),name ='cart-list-items')





]


