# -*- coding: utf-8 -*-
from .models import Match as match_model
from .models import MatchScore as matchscore_model
from .models import Round as round_model
from .models import Tournament as tournament_model
from django.core.exceptions import ObjectDoesNotExist
from graphql import GraphQLError
from rtcb.utils import extract_value_from_input
from ..team.models import Team as team_model
from rtcb.utils import extract_value_from_input


class MatchScoreService(object):

    def createMatchScore(self, input):

        team = extract_value_from_input(
            input=input,
            field_id='team',
            model_type='Team',
            model=team_model
        )

        matchScore = matchscore_model(
            team=team,
            score=input.get('score', 0),
            color=input.get('color', None)
        )
        matchScore.save()

        return matchScore


class MatchService(object):

    def createMatch(self, input):

        matchScoreService = MatchScoreService()

        # creo i match_score
        red_score = matchScoreService.createMatchScore({
            'team': input.get('red_team', None),
            'score': input.get('score', 0),
            'color': input.get('color', None)
        })
        blue_score = matchScoreService.createMatchScore({
            'team': input.get('blue_team', None),
            'score': input.get('score', 0),
            'color': input.get('color', None)
        })

        input_FK = {
            'match_day': ['match_day', 'Round', round_model],
            'tournament_id': ['tournament_id', 'Tournament', tournament_model]
        }

        for key in input_FK.keys():
            input[key] = extract_value_from_input(
                input=input,
                field_id=input_FK[key][0],
                model_type=input_FK[key][1],
                model=input_FK[key][2]
            )

        # initialize the match
        match = match_model(
            location=input.get('location', None),
            red_score=red_score,
            blue_score=blue_score,
            match_day=input.get('match_day', None),
            tournament_id=input.get('tournament_id', None),
            match_ended=input.get('match_ended', False)
        )
        match.save()

        # chiamate per inizializzare il match
        return match

    def createTournament(self, input):
        """ Crea un nuovo torneo.
        """
        # TOTEST
        name = input.get('name')

        new_tour = tournament_model(name=name)

        new_tour.save()
        return new_tour

    def update_tournament(self, input):
        """ Modifica dei dati di un torneo.
        """

        # TOTEST
        try:
            if input.get('tournament_id', None):
                tournament_to_update = extract_value_from_input(
                    input=input,
                    field_id='tournament_id',
                    model_type='Tournament',
                    model=tournament_model,
                )
        except ObjectDoesNotExist:
            raise GraphQLError(
                u'Problemi durante il recupero di una squadra.'
            )

        if input.get('name', None):
            tournament_to_update.name = input.get('name')

        tournament_to_update.save()
        return tournament_to_update

    def delete_tournament(self, input):
        """ Cancellazione di un torneo.
        """

        try:
            tour_to_delete = extract_value_from_input(
                input=input,
                field_id='tournament_id',
                model_type='Tournament',
                model=tournament_model,
            )
        except ObjectDoesNotExist:
            raise GraphQLError(
                u'Problemi durante il recupero di un torneo.'
            )

        return tour_to_delete.delete()
