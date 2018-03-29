# -*- coding: utf-8 -*-

from rtcb.team.models import Team
from faker import Faker


def create_teams(self):
    """ This function creates some Teams.
    """

    if self.flush:
        allTeams = Team.objects.all()
        for team in allTeams:
            team.delete()

    fake = Faker()

    for i in range(5):
        new_team = Team(
            name=fake.company()
        )

        new_team.save()
        # teams = Team.objects.all()
        # for team in teams:
        #     if team.players.count() < 2:
        #         new_player.team = team
        # new_player.save()
