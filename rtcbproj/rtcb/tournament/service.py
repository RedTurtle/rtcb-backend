# -*- coding: utf-8 -*-
from .models import Match as match_model
from .models import Tournament as tournament_model


class MatchService(object):

    def createMatch(self, input):
        match = match_model()
        match.save()
        return match

    def createTournament(self, input):
        """ Crea un nuovo torneo.
        """

        name = input.get('name')

        new_tour = tournament_model(name=name)

        new_tour.save()
        return new_tour
