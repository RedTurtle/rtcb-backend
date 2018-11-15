# -*- coding: utf-8 -*-
from graphene_django import DjangoObjectType
from .models import Match as match_model
from .models import MatchScore as matchscore_model

import graphene


class MatchScore(DjangoObjectType):
    class Meta:
        model = matchscore_model
        interfaces = (graphene.Node, )

    id_db = graphene.ID()

    def resolve_id_db(self, info, **input):
        """ Ritorna  l'ID del db """
        return self.id


class Match(DjangoObjectType):
    class Meta:
        model = match_model
        interfaces = (graphene.Node, )

    id_db = graphene.ID()

    def resolve_id_db(self, info, **input):
        """ Ritorna  l'ID del db """
        return self.id
