# -*- coding: utf-8 -*-

from .models import Team as TeamModel
from django.core.exceptions import ObjectDoesNotExist
from graphql import GraphQLError
from rtcb.authentication.models import User
from rtcb.utils import extract_value_from_input


class TeamService(object):

    def _get_player(self, user_id):
        """ Funzione di utilità per recuperare un utente in base all'id.
        """

        input_id = {
            'user': user_id,
        }

        player = extract_value_from_input(
            input=input_id,
            field_id='user',
            model_type='Player',
            model=User
        )

        return player

    def create_team(self, inputs):
        """Crea una nuova squadra (Team)
        """
        # TOTEST
        name = inputs.get('name')
        defender = extract_value_from_input(
            input=inputs,
            field_id='defender',
            model_type='User',
            model=User
        )
        striker = extract_value_from_input(
            input=inputs,
            field_id='striker',
            model_type='User',
            model=User
        )
        new_team = TeamModel(
            **{
                'name': name,
                'defender': defender,
                'striker': striker
            }
        )
        new_team.save()
        return new_team

    def update_team(self, inputs):
        """Aggiorna una squadra esistente (Team)

        inputs:
            dict con i parametri per l'aggiornamento
        """
        # TOTEST

        try:
            if inputs.get('team_id', None):
                team_to_update = extract_value_from_input(
                    input=inputs,
                    field_id='team_id',
                    model_type='Team',
                    model=TeamModel,
                )
        except ObjectDoesNotExist:
            raise GraphQLError(
                u'Problemi durante il recupero di una squadra.'
            )

        if inputs.get('name', None):
            team_to_update.name = inputs.get('name')
        if inputs.get('defender', None):
            team_to_update.defender = self._get_player(inputs.get('defender'))
        if inputs.get('striker', None):
            team_to_update.striker = self._get_player(inputs.get('striker'))

        team_to_update.save()
        return team_to_update
