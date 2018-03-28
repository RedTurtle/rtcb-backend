from django.db import models
from datetime import datetime

ROLES = (
    ('', ''),
    ('D', 'Defender'),
    ('S', 'Striker')
)


class Team(models.Model):
    team_name = models.CharField(max_length=50)


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=1,
        choices=ROLES,
        default=u'',
    )
    team = models.ForeignKey(
        Team,
        null=True,
        related_name="players",
        on_delete=models.SET_NULL
    )


class Tournament(models.Model):
    title = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )


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
