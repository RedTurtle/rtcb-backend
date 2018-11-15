# -*- coding: utf-8 -*-
from ..team.models import Team as team_model
from .models import Tournament as tournament_model
from django.core.exceptions import ObjectDoesNotExist
from graphql import GraphQLError
from rtcb.utils import extract_value_from_input


class TournamentService(object):

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
