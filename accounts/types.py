import graphene

from graphene_django import DjangoObjectType

from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','gender','phone_no']



class UserQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)
    
    def resolve_all_users(root,info):
        return User.objects.all()
    