# -*- coding: utf-8 -*-
from .models import Match as match_model


class MatchService(object):

    def createMatch(self, input):
        match = match_model()
        match.save()
        return match
