# -*- coding: utf-8 -*-
from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50)

    def __str__(self):
        return "<Team: {}>".format(self.team_name)
