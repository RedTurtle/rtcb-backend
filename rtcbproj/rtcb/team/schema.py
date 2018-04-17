import graphene
from graphene_django import DjangoObjectType
from .models import Team as TeamModel


class Team(DjangoObjectType):

    class Meta:
        model = TeamModel
        interfaces = (graphene.Node, )

