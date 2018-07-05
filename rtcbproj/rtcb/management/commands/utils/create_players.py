# -*- coding: utf-8 -*-

from rtcb.authentication.models import User
from faker import Faker
import random


def create_players(self):
    """ This function creates some Players.
    """

    allPlayers = User.objects.all()
    for player in allPlayers:
        if player.is_superuser is False:
            player.delete()

    fake = Faker()

    for i in range(10):
        name = fake.user_name()
        print('name: {0}'.format(name))
        new_player = User(
            first_name=name,
            username=name,
            last_name=fake.last_name(),
            role=random.sample(['D', 'S'],  1)[0],
            versatile=bool(random.getrandbits(1)),
        )
        new_player.save()
