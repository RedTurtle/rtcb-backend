# -*- coding: utf-8 -*-
from graphene_django import DjangoObjectType
from .models import Tournament as tournament_model

import graphene


class Tournament(DjangoObjectType):
    class Meta:
        model = tournament_model
        interfaces = (graphene.Node, )

    id_db = graphene.ID()

    def resolve_id_db(self, info, **input):
        """ Ritorna  l'ID del db """
        return self.id
