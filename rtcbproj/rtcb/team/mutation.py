# -*- coding: utf-8 -*-

import graphene
from .schema import Team
from graphene import relay
from .service import TeamService


class CreateTeam(relay.ClientIDMutation):
    """ Mutation for team creation
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


class UpdateTeam(relay.ClientIDMutation):
    """ Mutation for updating a Team infos
    """

    class Input:
        team_id = graphene.ID(required=True)
        name = graphene.String()
        defender = graphene.ID()
        striker = graphene.ID()

    ok = graphene.Boolean()
    team = graphene.Field(Team)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        teamservice = TeamService()
        updatedteam = teamservice.update_team(input)
        return UpdateTeam(
            team=updatedteam,
            ok=bool(updatedteam.id)
        )


class DeleteTeam(relay.ClientIDMutation):
    """ Mutation for deleting a Team
    """

    class Input:
        team_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        teamservice = TeamService()
        object_deleted = teamservice.delete_team(input)
        return DeleteTeam(ok=True if (object_deleted[0] == 1) else False)
