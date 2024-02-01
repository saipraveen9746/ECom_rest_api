from django.shortcuts import render
from .serializers import ProductSerializer,CartSerializer,CartItemSerializer
from rest_framework import generics,status
from .models import Product,Cart,CartProduct
from rest_framework.response import responses
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
# Create your views here.




class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)
class ProductDetailview(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#

# class AddtoCartView(APIView):
#     authentication_classes = [JWTAuthentication]
#     def post(self,request):
#         if not request.user.is_authenticated:
#             return Response({'error':'User is not authenticated'},status=status.HTTP_401_UNAUTHORIZED)
#         product_id = request.data.get('product_id')
#         quantity = request.data.get('quantity')
#         try:
#             product = Product.objects.get(product_id)
#             cart_item = Cart(user = request.user,product = product,quantity=quantity)
#             serializer = CartSerializer(data= request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         except ObjectDoesNotExist:
#             return Response({'error':'product not found'},status.HTTP_404_NOT_FOUND)

    # def get(self,request):
    #     quaryset = Cart.objects.all()
    #     serializer = CartSerializer(quaryset,many=True)
    #     return Response(serializer.data)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# class AddToCartView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self,request):
#
#
#         cart_item, created = Cart.objects.get_or_create(user=request.user)
#         product_id = request.data.get('product_id')
#         print("###################",product_id)
#         # quantity = request.data.get('quantity')
#         try:
#             product = Product.objects.get(pk=product_id)
#             print('$$$$$$$$$$$$$$$',product)
#         except ObjectDoesNotExist:
#             return Response({'error':'product not found'},status=status.HTTP_404_NOT_FOUND)
#
#         cart_item, created = CartProduct.objects.get_or_create(cart=cart_item,product=product,)
#
#         # cart_item.quantity += quantity
#         # cart_item.save()
#
#         serializer = CartSerializer(cart_item)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=False,methods=['get'])
    def my_cart(self,request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer =CartSerializer(cart)
        return Response(serializer.data)
    @action(detail=False,methods=['post'])
    def add_to_cart(self,request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity',1))

        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'error':'Product not found'},status=404)
        cart_item,created = CartProduct.objects.get_or_create(cart=cart,product=product)
        cart_item.quantity += quantity
        cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def update_cart_item(self,request):
        cart_item_id = request.data.get('cart_item_id')
        quantity = int(request.data.get('quantity',1))

        try:
            cart_item = CartProduct.objects.get(pk=cart_item_id)
        except CartProduct.DoesNotExist:
            return Response({'error':'Cart item not found'},status= 404)

        cart_item.quantity= quantity
        cart_item.save()

        serializer = CartSerializer(cart_item.cart)
        return Response(serializer.data)

    # @action(detail=False, methods=['delete'])
    # def remove_from_cart(self,request):
    #     cart_item_id =request.data.get()




