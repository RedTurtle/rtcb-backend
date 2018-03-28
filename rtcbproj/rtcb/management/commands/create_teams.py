# -*- coding: utf-8 -*-

from rtcb.models import Team
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
            team_name=fake.company()
        )

        new_team.save()
