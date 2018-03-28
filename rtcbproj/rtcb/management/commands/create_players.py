# -*- coding: utf-8 -*-

from rtcb.models import Player
from rtcb.models import Team
from faker import Faker
import random


def create_players(self):
    """ This function creates some Players.
    """

    if self.flush:
        allPlayers = Player.objects.all()
        for player in allPlayers:
            player.delete()

    fake = Faker()

    for i in range(10):
        new_player = Player(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            role=random.sample(['D', 'S'],  1)[0]

        )

        new_player.save()
        teams = Team.objects.all()
        for team in teams:
            if team.players.count() < 2:
                new_player.team = team
        new_player.save()
