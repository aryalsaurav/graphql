from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from accounts.models import User

from .serializers import UserCreateSerializer



class UserCreateView(APIView):
    permission_classes = [AllowAny]
    
    def dispatch(self, request, *args, **kwargs):
        self.model = User
        self.serializer_class = UserCreateSerializer
        return super().dispatch(request, *args, **kwargs)
    
    
    
    @extend_schema(
        request = UserCreateSerializer,
        responses = {201:UserCreateSerializer}
    )
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'message':'success',
                'status':201,
                'data':serializer.data
            }
            return Response(context,status=201)
        return Response({"details":serializer.errors},status=400)