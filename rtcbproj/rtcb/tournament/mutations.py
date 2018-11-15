# -*- coding: utf-8 -*-
from .schema import Tournament
from .service import TournamentService

import graphene


class CreateTournament(graphene.ClientIDMutation):
    """ Creazione di un torneo.
    """

    class Input:
        name = graphene.String()

    ok = graphene.Boolean()
    tournament = graphene.Field(Tournament)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        tourService = TournamentService()
        tournament = tourService.createTournament(input=input)
        return CreateTournament(tournament=tournament, ok=bool(tournament.id))


class UpdateTournament(graphene.ClientIDMutation):
    """ Mutation for updating a Tournament infos.
    """

    class Input:
        tournament_id = graphene.ID(required=True)
        name = graphene.String()

    ok = graphene.Boolean()
    tournament = graphene.Field(Tournament)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        tourService = TournamentService()
        updatedtournament = tourService.update_tournament(input)
        return UpdateTournament(
            tournament=updatedtournament,
            ok=bool(updatedtournament.id)
        )


class DeleteTournament(graphene.ClientIDMutation):
    """ Mutation for deleting a Tournament
    """

    class Input:
        tournament_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        tourService = TournamentService()
        object_deleted = tourService.delete_tournament(input)
        return DeleteTournament(ok=True if (object_deleted[0] == 1) else False)
