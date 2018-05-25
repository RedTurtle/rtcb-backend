# -*- coding: utf-8 -*-
from graphene_django import DjangoObjectType
from .models import Match as match_model
from .models import MatchScore as matchscore_model

import graphene


class Match(DjangoObjectType):
    class Meta:
        model = match_model
        interfaces = (graphene.Node, )


class MatchScore(DjangoObjectType):
    class Meta:
        model = matchscore_model
        interfaces = (graphene.Node, )
