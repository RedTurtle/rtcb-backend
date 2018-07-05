# -*- coding: utf-8 -*-

import graphene
from .schema import User
from graphene import relay
from .service import UserService


class CreateUser(relay.ClientIDMutation):
    """ Mutation for user creation
    """

    class Input:
        email = graphene.String(required=False)
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.String(required=True)
        versatile = graphene.Boolean(required=False)
    
    ok = graphene.Boolean()
    user = graphene.Field(User)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        userservice = UserService()
        newuser = userservice.create_user(input)
        return CreateUser(user=newuser, ok=bool(newuser.id))


class UpdateUser(relay.ClientIDMutation):
    """ Mutation for updating a User infos
    """

    class Input:
        user_id = graphene.ID(required=True)
        name = graphene.String()
        defender = graphene.ID()
        striker = graphene.ID()

    ok = graphene.Boolean()
    user = graphene.Field(User)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        userservice = UserService()
        updateduser = userservice.update_user(input)
        return UpdateUser(
            user=updateduser,
            ok=bool(updateduser.id)
        )


class DeleteUser(relay.ClientIDMutation):
    """ Mutation for deleting a User
    """

    class Input:
        user_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        userservice = UserService()
        object_deleted = userservice.delete_user(input)
        return DeleteUser(ok=True if (object_deleted[0] == 1) else False)
