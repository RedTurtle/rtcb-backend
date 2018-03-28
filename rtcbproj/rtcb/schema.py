# -*- coding: utf-8 -*-
from graphene_django import DjangoConnectionField, filter

import graphene


class Query(graphene.ObjectType):

    # NODO GENERICO
    node = graphene.Node.Field()


class Mutation(graphene.ObjectType):
    """ Mutation entry point graphQL.
    """
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
