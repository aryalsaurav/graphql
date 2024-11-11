from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from accounts.models import User

from .serializers import UserCreateSerializer,LoginSerializer



class LoginView(APIView):
    permission_classes = [AllowAny]
    
    @extend_schema(
        request = LoginSerializer,
        responses={
            200: {
                "type": "object",
                "properties": {
                    "access": {"type": "string", "description": "JWT access token"},
                    "refresh": {"type": "string", "description": "JWT refresh token"}
                },
                "description": "Successful login returns JWT access and refresh tokens"
            },
            401: {
                "type": "object",
                "properties": {
                    "detail": {"type": "string", "example": "Invalid credentials"}
                },
                "description": "Error response for invalid credentials"
            }
        }
    )
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            refresh = RefreshToken.for_user(user)
            context = {
                'status':200,
                'message':"Logged in successfully !!!",
                'data': {
                    'access':str(refresh.access_token),
                    'refresh':str(refresh)
                }
            }
            return Response(context,status=200)
        return Response({"details":'Invalid Username or password'},status=401)



class UserCreateView(APIView):
    permission_classes = [AllowAny]
    
    def dispatch(self, request, *args, **kwargs):
        self.model = User
        self.serializer_class = UserCreateSerializer
        return super().dispatch(request, *args, **kwargs)
    
    
    
    @extend_schema(
        request = UserCreateSerializer,
        responses = {201:UserCreateSerializer},
        methods=["POST"]
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