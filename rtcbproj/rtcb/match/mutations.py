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
