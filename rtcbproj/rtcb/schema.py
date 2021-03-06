# -*- coding: utf-8 -*-
from .authentication.mutation import CreateUser
from .authentication.schema import User
from .match import mutations as MatchMutations
from .match.schema import Match
from .team.mutation import CreateTeam, UpdateTeam, DeleteTeam
from .team.schema import Team
from .tournament import mutations as TournamentMutations
from .tournament.schema import Tournament
from graphene_django import DjangoConnectionField

import graphene


class Query(graphene.ObjectType):

    # NODO GENERICO
    node = graphene.Node.Field()

    # Player
    players = DjangoConnectionField(User, description="all players")
    player = graphene.Node.Field(User)

    # Team
    # Player
    teams = DjangoConnectionField(Team, description="all teams")
    team = graphene.Node.Field(Team)

    # Tournament
    tournaments = DjangoConnectionField(
        Tournament, description="all tournaments"
    )
    tournament = graphene.Node.Field(Tournament)

    # match
    matches = DjangoConnectionField(Match, description="all matches")
    match = graphene.Node.Field(Match)


class Mutation(graphene.ObjectType):
    """ Mutation entry point graphQL"""

    create_team = CreateTeam.Field()
    update_team = UpdateTeam.Field()
    delete_team = DeleteTeam.Field()
    create_user = CreateUser.Field()
    # update_user = UpdateUser.Field()
    # delete_user = DeleteUser.Field()
    create_match = MatchMutations.CreateMatch.Field()
    update_match = MatchMutations.UpdateMatch.Field()
    delete_match = MatchMutations.DeleteMatch.Field()
    create_tournament = TournamentMutations.CreateTournament.Field()
    update_tournament = TournamentMutations.UpdateTournament.Field()
    delete_tournament = TournamentMutations.DeleteTournament.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
