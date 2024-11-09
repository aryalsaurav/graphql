import graphene




query_list = []

class Query(*query_list,graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)