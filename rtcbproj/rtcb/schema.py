# -*- coding: utf-8 -*-
from .authentication.models import User as player_model
from .team.mutation import CreateTeam, UpdateTeam, DeleteTeam
from .authentication.mutation import CreateUser
# , UpdateUser, DeleteUser
from .authentication.schema import User
from .team.schema import Team
from .tournament import mutations as MatchMutations
from .tournament.schema import Tournament
from graphene_django import DjangoConnectionField
from graphene_django import DjangoObjectType

import graphene


class Query(graphene.ObjectType):

    # NODO GENERICO
    node = graphene.Node.Field()

    # Player
    players = DjangoConnectionField(
        User,
        description="all players"
    )
    player = graphene.Node.Field(User)

    # Team
    # Player
    teams = DjangoConnectionField(
        Team,
        description="all teams"
    )
    team = graphene.Node.Field(Team)

    tournaments = DjangoConnectionField(
        Tournament,
        description="all tournaments"
    )
    tournament = graphene.Node.Field(Tournament)


class Mutation(graphene.ObjectType):
    """ Mutation entry point graphQL"""

    create_team = CreateTeam.Field()
    update_team = UpdateTeam.Field()
    delete_team = DeleteTeam.Field()
    create_user = CreateUser.Field()
    # update_user = UpdateUser.Field()
    # delete_user = DeleteUser.Field()
    create_match = MatchMutations.CreateMatch.Field()
    create_tournament = MatchMutations.CreateTournament.Field()
    update_tournament = MatchMutations.UpdateTournament.Field()
    delete_tournament = MatchMutations.DeleteTournament.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
