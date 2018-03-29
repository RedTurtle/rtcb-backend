# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from .utils.create_players import create_players
from .utils.create_teams import create_teams
from .utils.tournament import create_tournament


class Command(BaseCommand):
    help = """Populate the db for the Legionella-Backend project
    with fake data."""

    flush = True

    def handle(self, *args, **options):
        create_players(self)
        create_tournament(self)
        create_teams(self)
