# -*- coding: utf-8 -*-
from django.db import models
from rtcb.authentication.models import User


class Team(models.Model):
    name = models.CharField(max_length=50)

    defender = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="defender_player",
    )

    striker = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name="striker_player",
    )

    tournament = models.ForeignKey(
        'Tournament',
        null=True,
        on_delete=models.SET_NULL,
        # related_name="toru",
    )

    def __str__(self):
        return "Team: {}".format(self.name)
