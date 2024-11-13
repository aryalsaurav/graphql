from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from accounts.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username','password','first_name','last_name','gender','phone_no']
        extra_kwargs = {
            'password':{'write_only':True},
            'username':{'read_only':True}
        }
    
    
    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name','gender','phone_no']



class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    
    
    def validate(self,validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        
        user = authenticate(email=email,password=password)
        
        if not user:
            raise serializers.ValidationError("Incorrect email or password")
        validated_data['user'] = user
        return validated_data
        
        