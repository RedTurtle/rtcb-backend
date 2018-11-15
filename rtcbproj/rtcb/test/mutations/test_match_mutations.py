# -*- coding: utf-8 -*-
from ...match.mutations import CreateMatch

import pytest
import graphene


def test_no_mutate_and_get_payload():
    with pytest.raises(AssertionError) as excinfo:

        class MyMutation(graphene.ClientIDMutation):
            pass

    assert "MyMutation.mutate_and_get_payload method is required in a ClientIDMutation." == str(
        excinfo.value)


def test_create_mutation():
    fields = CreateMatch._meta.fields
    assert list(fields.keys()) == ['ok', 'match', 'client_mutation_id']
    assert CreateMatch._meta.name == "CreateMatchPayload"
    # assert isinstance(fields['phrase'], Field)
    # field = SaySomething.Field()
    # assert field.type == SaySomething
    # assert list(field.args.keys()) == ['input']
    # assert isinstance(field.args['input'], Argument)
    # assert isinstance(field.args['input'].type, NonNull)
    # assert field.args['input'].type.of_type == SaySomething.Input
    # assert isinstance(fields['client_mutation_id'], Field)
    # assert fields['client_mutation_id'].name == 'clientMutationId'
    # assert fields['client_mutation_id'].type == String
