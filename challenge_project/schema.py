import graphene
from people.schema import Query as PeopleQuery


class Query(PeopleQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
