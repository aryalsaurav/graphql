import graphene


from .types import UserQuery

query_list = [UserQuery]

class Query(*query_list,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)