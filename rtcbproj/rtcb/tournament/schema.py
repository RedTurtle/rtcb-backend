# -*- coding: utf-8 -*-
from graphene_django import DjangoObjectType
from .models import Match as match_model

import graphene


class Match(DjangoObjectType):
    class Meta:
        model = match_model
        interfaces = (graphene.Node, )
