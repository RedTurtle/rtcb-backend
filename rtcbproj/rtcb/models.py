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


class Days(models.Model):
    date_matchs = models.DateField(
        'data del rapporto di campionamento',
        default=datetime.today,
        blank=True,
        null=True
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
    day_match = models.ForeignKey(
        Days,
        related_name='day_match',
        on_delete=models.CASCADE,
        null=True,
    )
