# -*- coding: utf-8 -*-

from rtcb.tournament.models import Tournament


def create_tournament(self):
    new_tournament = Tournament(
        name="Campionato mondiale di Calcino!",
    )

    new_tournament.save()
