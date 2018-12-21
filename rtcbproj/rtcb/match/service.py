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
            field_id="matchscore_id",
            model_type="MatchScore",
            model=matchscore_model,
        )

    def _getTeam(self, input):
        return extract_value_from_input(
            input=input, field_id="team", model_type="Team", model=team_model
        )

    def createMatchScore(self, input):
        team = self._getMatchTeam(input)
        matchScore = matchscore_model(
            team=team,
            score=input.get("score", 0),
            color=input.get("color", None),
        )
        matchScore.save()

        return matchScore

    def updateMatchScore(self, input):
        matchscore_to_update = self._getMatchScore(input)
        if input.get("team", None):
            team_to_update = self._getTeam(input)
            matchscore_to_update.team = team_to_update
        if input.get("score", None):
            matchscore_to_update.score = input.get("score", None)
        if input.get("color", None):
            matchscore_to_update.color = input.get("color", None)

        matchscore_to_update.save()
        return matchscore_to_update

    def updateScore(self, input):
        try:
            if input.get("team", None):
                matchscore_to_update = self._getMatchScore(input)
        except ObjectDoesNotExist:
            raise GraphQLError(
                u"Problemi durante il recupero di un matchscore."
            )

        matchscore_to_update.score += 1
        matchscore_to_update.save()
        return matchscore_to_update


class MatchService(object):
    def _getMatch(self, input):
        return extract_value_from_input(
            input=input,
            field_id="match_id",
            model_type="Match",
            model=match_model,
        )

    def _getTeam(self, team_id):
        return extract_value_from_input(
            input={}, field_id="team", model_type="Team", model=team_model
        )

    def checkDuplicate(self, input):
        """
        Verifica che non siano stati inseriti due team uguali
        """
        if "red_team" not in input or "blue_team" not in input:
            # siamo nell'update..non sono campi obbligatori
            return
        if input.get("red_team") == input.get("blue_team"):
            raise GraphQLError(
                u"Non si può impostare due volte la stessa squadra per un match." # noqa
            )

    def createMatch(self, input):

        matchScoreService = MatchScoreService()

        self.checkDuplicate(input)

        # creo i match_score
        red_score = matchScoreService.createMatchScore(
            {"team": input.get("red_team", None), "score": 0, "color": "red"}
        )
        blue_score = matchScoreService.createMatchScore(
            {"team": input.get("blue_team", None), "score": 0, "color": "blue"}
        )

        input_FK = {
            "tournament_id": ["tournament_id", "Tournament", tournament_model]
        }

        for key in input_FK.keys():
            input[key] = extract_value_from_input(
                input=input,
                field_id=input_FK[key][0],
                model_type=input_FK[key][1],
                model=input_FK[key][2],
            )

        # initialize the match
        match = match_model(
            location=input.get("location", None),
            red_score=red_score,
            blue_score=blue_score,
            tournament_id=input.get("tournament_id", None),
            match_ended=input.get("match_ended", False),
        )
        match.save()

        # chiamate per inizializzare il match
        return match

    def updateMatch(self, input):

        skip_fields = ["match_id", "red_team", "blue_team"]

        self.checkDuplicate(input)
        match_to_update = self._getMatch(input)

        for k, v in input.items():
            if k in skip_fields:
                continue
            setattr(match_to_update, k, v)
        matchScoreService = MatchScoreService()
        if "red_team" in input:
            red_score = getattr(match_to_update, "red_score", None)
            matchScoreService.updateMatchScore(
                {"matchscore_id": red_score.id, "team": input["red_team"]}
            )
        if "blue_team" in input:
            blue_score = getattr(match_to_update, "blue_score", None)
            matchScoreService.updateMatchScore(
                {"matchscore_id": blue_score.id, "team": input["blue_team"]}
            )
        match_to_update.save()

        # BBB: da verificare..qui si fa una query forse inutile.
        return self._getMatch(input)

    def deleteMatch(self, input):
        """
        Metodo per la cancellazione di un match che non è ancora cominciato.
        Il match è eliminabile quando non è ancora cominciato e quando non fa
        parte di un torneo.
        """

        match = extract_value_from_input(
            input=input,
            field_id="match_id",
            model_type="Match",
            model=match_model,
        )

        # controllo che il match sia cancellabile
        if match.tournament or match.match_started:
            # il match è iniziato
            raise GraphQLError(u"Il Match non si può eliminare.")

        # se lo è elimino il match
        return match.delete()
