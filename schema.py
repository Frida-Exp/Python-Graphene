import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(info, kwargs):
        return 'Hello'