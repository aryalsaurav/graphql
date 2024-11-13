from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from products.models import Category,Product,OrderItem,Order
from .serializers import (
    CategorySerializer,
    ProdcutSerializer,
    OrderItemSerializer,
    OrderSerializer
)

from accounts.models import User



class CategoryCreateView(APIView):
    permission_classes = [AllowAny]
    
    def dispatch(self,request,*args,**kwargs):
        self.model = Category
        self.serializer_class = CategorySerializer
        self.queryset = self.model.objects.all()
        return super().dispatch(request,*args,**kwargs)
    
    
    @extend_schema(
        request = CategorySerializer,
        responses = {201 : CategorySerializer}
    )
    def post(self,request):
        requested_data = request.data
        serializer = self.serializer_class(data=requested_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)




class ProductCreateView(APIView):
    permission_classes = [AllowAny]
    
    def dispatch(self,request,*args,**kwargs):
        self.model = Product
        self.serializer_class = ProdcutSerializer
        self.queryset = self.model.objects.all()
        return super().dispatch(request,*args,**kwargs)
    
    
    @extend_schema(
        request = ProdcutSerializer,
        responses = {201 : ProdcutSerializer}
    )
    def post(self,request):
        requested_data = request.data
        serializer = self.serializer_class(data=requested_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)




class OrderItemCreateView(APIView):
    permission_classes = [AllowAny]
    
    def dispatch(self,request,*args,**kwargs):
        self.model = OrderItem
        self.serializer_class = OrderItemSerializer
        self.queryset = self.model.objects.all()
        return super().dispatch(request,*args,**kwargs)
    
    
    @extend_schema(
        request = OrderItemSerializer,
        responses = {201 : OrderItemSerializer}
    )
    def post(self,request):
        requested_data = request.data
        serializer = self.serializer_class(data=requested_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)
    
    



class OrderCreateView(APIView):
    permission_classes = [AllowAny]
    
    def dispatch(self,request,*args,**kwargs):
        self.model = Order
        self.serializer_class = OrderSerializer
        self.queryset = self.model.objects.all()
        return super().dispatch(request,*args,**kwargs)
    
    
    @extend_schema(
        request = OrderSerializer,
        responses = {201 : OrderSerializer}
    )
    def post(self,request):
        requested_data = request.data
        serializer = self.serializer_class(data=requested_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)