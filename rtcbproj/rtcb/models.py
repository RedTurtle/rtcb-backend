from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50)


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.ForeignKey(
        Team,
        null=True,
        related_name="players",
        on_delete=models.SET_NULL
    )


class Match(models.Model):
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
