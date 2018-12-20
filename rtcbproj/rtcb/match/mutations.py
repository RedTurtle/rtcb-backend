# -*- coding: utf-8 -*-

from .schema import Match
from .service import MatchService

import graphene


class CreateMatch(graphene.ClientIDMutation):
    """ Creazione di una nuova partita """

    class Input:
        location = graphene.String()
        red_team = graphene.ID(required=True)
        blue_team = graphene.ID(required=True)
        tournament_id = graphene.ID()
        match_ended = graphene.Boolean()

    ok = graphene.Boolean()
    match = graphene.Field(Match)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        match = MatchService().createMatch(input=input)
        return CreateMatch(match=match, ok=bool(match.id))


class UpdateMatch(graphene.ClientIDMutation):
    """ Aggiorna una partita """

    class Input:
        match_id = graphene.ID(required=True)
        location = graphene.String()
        red_team = graphene.ID()
        blue_team = graphene.ID()
        tournament_id = graphene.ID()
        match_ended = graphene.Boolean()

    ok = graphene.Boolean()
    match = graphene.Field(Match)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        matchService = MatchService()
        updated_match = matchService.updateMatch(input)
        return UpdateMatch(match=updated_match, ok=bool(updated_match.id))
