# -*- coding: utf-8 -*-
from django.db import models
from rtcb.team.models import Team


class Tournament(models.Model):
    name = models.CharField(
        verbose_name="Tournament name",
        max_length=50,
    )

    def __str__(self):
        return self.name


class Round(models.Model):
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


class Match(models.Model):
    class Meta:
        verbose_name = "match"
        verbose_name_plural = "matches"

    location = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    team_a = models.ForeignKey(
        Team,
        related_name="matches_a",
        null=True,
        on_delete=models.SET_NULL
    )

    team_b = models.ForeignKey(
        Team,
        related_name="matches_b",
        null=True,
        on_delete=models.SET_NULL
    )

    match_day = models.ForeignKey(
        Round,
        related_name='match_day',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return "Match: {} VS. {}".format(
            self.team_a.team_name,
            self.team_b.team_name,
            self.match_day,
        )
