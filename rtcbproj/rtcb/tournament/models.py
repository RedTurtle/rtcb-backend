# -*- coding: utf-8 -*-
from django.db import models
from rtcb.team.models import Team


class Tournament(models.Model):
    name = models.CharField(
        verbose_name="Tournament name",
        max_length=50,
    )

    teams = models.ManyToManyField(
        Team,
        verbose_name="Squadre",
        related_name="tournaments",
        related_query_name="tournament",
    )

    def __str__(self):
        return self.name


class Round(models.Model):
    """ Giornata del torneo
    """

    title = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    counter = models.PositiveIntegerField(
        default=0
    )

    tournament = models.ForeignKey(
        Tournament,
        related_name='tournament',
        null=True,
        on_delete=models.CASCADE,
    )
