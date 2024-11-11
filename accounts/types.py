import graphene

from graphene_django import DjangoObjectType

from django.db.models import Q

from .models import User


class GenderEnum(graphene.Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHERS = "Others"

class UserType(DjangoObjectType):
    gender = graphene.Field(GenderEnum)
    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','gender','phone_no']



class UserQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_id = graphene.List(UserType,id=graphene.Int(required=False),gender=graphene.String(required=False))
    filtered_user = graphene.List(UserType, filters=graphene.JSONString(required=False))
    
    def resolve_all_users(root,info):
        return User.objects.all()
    
    def resolve_user_by_id(root,info,**kwargs):
        id = kwargs.get('id')
        gender = kwargs.get('gender')
        query = Q()
        if id:
            query &= Q(id=id)
        if gender:
            query &= Q(gender=gender)
        return User.objects.filter(query)
    
    
    def resolve_filtered_user(root,info,filters):
        users = User.objects.all()
        if 'first_name' in filters.keys():
            users = users.filter(first_name__icontains=filters['first_name'])

        return users
        