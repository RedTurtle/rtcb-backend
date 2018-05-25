# -*- coding: utf-8 -*-
from graphene_django import DjangoConnectionField
from graphene_django import DjangoObjectType
from .authentication.models import User as player_model
from .team.models import Team as team_model
from .tournament import mutations as MatchMutations
from .tournament.schema import Match

import graphene


class Player(DjangoObjectType):
    class Meta:
        model = player_model
        interfaces = (graphene.Node, )


class Team(DjangoObjectType):
    class Meta:
        model = team_model
        interfaces = (graphene.Node, )


class Query(graphene.ObjectType):

    # NODO GENERICO
    node = graphene.Node.Field()

    # Player
    players = DjangoConnectionField(
        Player,
        description="all players"
    )
    player = graphene.Node.Field(Player)

    # Team
    # Player
    teams = DjangoConnectionField(
        Team,
        description="all team"
    )
    team = graphene.Node.Field(Team)

    # matchs = DjangoConnectionField(
    #     Match,
    #     description="all match"
    # )
    # match = graphene.Node.Field(Match)


class Mutation(graphene.ObjectType):
    """ Mutation entry point graphQL"""

    create_match = MatchMutations.CreateMatch.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
