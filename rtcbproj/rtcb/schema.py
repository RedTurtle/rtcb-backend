# -*- coding: utf-8 -*-
from graphene_django import DjangoConnectionField
from graphene_django import DjangoObjectType
from .tournament.models import Match as match_model
from .authentication.models import User as player_model
from .team.models import Team as team_model
from .team.mutation import CreateTeam
from .team.schema import Team
import graphene


class Player(DjangoObjectType):
    class Meta:
        model = player_model
        interfaces = (graphene.Node, )


class Match(DjangoObjectType):
    class Meta:
        model = match_model
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


class Mutation(graphene.ObjectType):
    """
    Mutation entry point graphQL.
    """
    create_team = CreateTeam.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
