import graphene
from graphene_django import DjangoObjectType

from .models import Person, Address


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = ('number', 'street', 'city', 'state')


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = ('email', 'name', 'address')


class Query(graphene.ObjectType):
    people = graphene.List(PersonType, page_size=graphene.Int(), page_offset=graphene.Int())

    def resolve_people(self, info, page_size=None, page_offset=None, **kwargs):
        qs = Person.objects.select_related('address').all()
        if page_offset is not None:
            qs = qs[page_offset:]
        if page_size is not None:
            qs = qs[:page_size]
        return qs


schema = graphene.Schema(query=Query)
