# -*- coding: utf-8 -*-
from django.db import models
from rtcb.team.models import Team
from rtcb.tournament.models import Tournament


class MatchScore(models.Model):

    team = models.ForeignKey(
        Team, null=True, on_delete=models.SET_NULL, related_name="team_id"
    )
    score = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):
        return "MatchScore: {} - {}".format(self.team.name, self.score)


class Match(models.Model):
    """ Modello che descrive una singola partita
    """

    class Meta:
        verbose_name = "match"
        verbose_name_plural = "matches"

    location = models.CharField(
        max_length=50,
        null=True,
        default="Sala Relax",
        verbose_name="Location",
        blank=True,
    )

    red_score = models.ForeignKey(
        MatchScore,
        related_name="red_score",
        null=True,
        on_delete=models.CASCADE,
    )

    blue_score = models.ForeignKey(
        MatchScore,
        related_name="blue_score",
        null=True,
        on_delete=models.CASCADE,
    )

    tournament = models.ForeignKey(
        Tournament, null=True, on_delete=models.CASCADE, related_name="match"
    )

    match_ended = models.BooleanField(
        default=False, verbose_name="Is the match ended?"
    )

    def __str__(self):
        return "Match: {} VS. {}".format(
            self.red_score.team, self.blue_score.team
        )
