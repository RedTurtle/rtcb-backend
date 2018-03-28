# -*- coding: utf-8 -*-

from rtcb.models import Player
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
            last_name=fake.last_name_male(),
            role=random.sample(['D', 'S'],  1)[0]

        )

        new_player.save()
