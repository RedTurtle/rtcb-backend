# -*- coding: utf-8 -*-
from .models import User as UserModel
from django.core.exceptions import ObjectDoesNotExist
from graphql import GraphQLError
from rtcb.utils import extract_value_from_input
from django.contrib.auth.hashers import make_password


class UserService(object):

    def create_user(self, inputs):
        """Crea un nuovo user
        """
        # TOTEST
        params = inputs.copy()
        if 'password' in params:
            params['password'] = make_password(params['password'])
        new_user = UserModel.objects.create_user(**params)
        new_user.save()
        return new_user

    # def update_user(self, inputs):
    #     """Aggiorna una squadra esistente (User)

    #     inputs:
    #         dict con i parametri per l'aggiornamento
    #     """
    #     # TOTEST

    #     try:
    #         if inputs.get('user_id', None):
    #             user_to_update = extract_value_from_input(
    #                 input=inputs,
    #                 field_id='user_id',
    #                 model_type='User',
    #                 model=UserModel,
    #             )
    #     except ObjectDoesNotExist:
    #         raise GraphQLError(
    #             u'Problemi durante il recupero di una squadra.'
    #         )

    #     if inputs.get('name', None):
    #         user_to_update.name = inputs.get('name')
    #     if inputs.get('defender', None):
    #         user_to_update.defender = self._get_player(inputs.get('defender'))
    #     if inputs.get('striker', None):
    #         user_to_update.striker = self._get_player(inputs.get('striker'))

    #     user_to_update.save()
    #     return user_to_update

    # def delete_user(self, inputs):
    #     try:
    #         user_to_delete = extract_value_from_input(
    #             input=inputs,
    #             field_id='user_id',
    #             model_type='User',
    #             model=UserModel,
    #         )
    #     except ObjectDoesNotExist:
    #         raise GraphQLError(
    #             u'Problemi durante il recupero di una squadra.'
    #         )

    #     return user_to_delete.delete()
