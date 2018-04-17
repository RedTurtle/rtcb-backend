# -*- coding: utf-8 -*-

import graphene
from .schema import Team
from graphene import relay
from .models import Team as TeamModel
from .service import TeamService
from rtcb.utils import extract_value_from_input

class CreateTeam(relay.ClientIDMutation):
    """
    Mutation to team creation
    """

    class Input:
        name = graphene.String(required=True)
        defender = graphene.ID(required=True)
        striker = graphene.ID(required=True)

    ok = graphene.Boolean()
    team = graphene.Field(Team)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        teamservice = TeamService()
        newteam = teamservice.create_team(input)
        return CreateTeam(team=newteam, ok=bool(newteam.id))