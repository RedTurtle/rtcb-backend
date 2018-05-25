# -*- coding: utf-8 -*-
from ...tournament.mutations import CreateMatch
from ...schema import schema
from ...management.commands import populate
from django.test import TestCase

import pytest
import graphene


def test_no_mutate_and_get_payload():
    with pytest.raises(AssertionError) as excinfo:

        class MyMutation(graphene.ClientIDMutation):
            pass

    assert "MyMutation.mutate_and_get_payload method is required in a ClientIDMutation." == str(  # noqa
        excinfo.value)


def test_mutation_input():
    Input = CreateMatch.Input
    fields = Input._meta.fields
    assert list(fields.keys()) == [
        'location', 'red_team', 'blue_team',
        'match_day', 'tournament_id', 'match_ended', 'client_mutation_id']


def populatedb_for_testing():
    pop = populate.Command()
    opts = {
        'flush': True,
    }
    pop.handle(**opts)


class TestMutation(TestCase):

    def setUp(self):
        """
        Excecuted at the very start of the test suite.
        """
        populatedb_for_testing()

    def tearDown(self):
        """
        Metti qui quello che vuoi venga eseguito al termine del test.
        """

    def test_prova_mutation(self):
        executed = schema.execute(
            'mutation {createMatch(input: {redTeam: "1", blueTeam: "1"}){ok, match{id, redTeam{id}}}}'  # noqa
        )
        assert not executed.errors
