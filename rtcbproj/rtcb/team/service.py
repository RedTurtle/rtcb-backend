# -*- coding: utf-8 -*-

from .models import Team as TeamModel
from rtcb.authentication.models import User
from rtcb.utils import extract_value_from_input


class TeamService(object):

    def create_team(self, inputs):
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
