import graphene
from apps.users.schema import Query as UserQuery
from apps.news.schema import Query as NewsQuery

class Query(UserQuery, NewsQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
