# -*- coding: utf-8 -*-
from ..team.models import Team as team_model
from .models import Match as match_model
from .models import MatchScore as matchscore_model
from .models import Tournament as tournament_model
from django.core.exceptions import ObjectDoesNotExist
from graphql import GraphQLError
from rtcb.utils import extract_value_from_input


class MatchScoreService(object):

    def _getMatchScore(self, input):
        return extract_value_from_input(
            input=input,
            field_id='team',
            model_type='Team',
            model=team_model
        )

    def createMatchScore(self, input):
        team = self._getMatchScore(input)
        matchScore = matchscore_model(
            team=team,
            score=input.get('score', 0),
            color=input.get('color', None)
        )
        matchScore.save()

        return matchScore

    def updateMatchScore(self, input):
        try:
            if input.get('team', None):
                matchscore_to_update = self._getMatchScore(input)
        except ObjectDoesNotExist:
            raise GraphQLError(
                u'Problemi durante il recupero di un matchscore.'
            )

        if input.get('score', None):
            matchscore_to_update.score = input.get('score', None)
        if input.get('color', None):
            matchscore_to_update.color = input.get('color', None)

        matchscore_to_update.save()
        return matchscore_to_update

    def updateScore(self, input):
        try:
            if input.get('team', None):
                matchscore_to_update = self._getMatchScore(input)
        except ObjectDoesNotExist:
            raise GraphQLError(
                u'Problemi durante il recupero di un matchscore.'
            )

        matchscore_to_update.score += 1
        matchscore_to_update.save()
        return matchscore_to_update


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

    def updateMatch(self, input):
        pass

    def deleteMatch(self, input):
        pass
