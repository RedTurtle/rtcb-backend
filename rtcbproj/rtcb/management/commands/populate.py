# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from .create_players import create_players


class Command(BaseCommand):
    help = """Populate the db for the Legionella-Backend project
    with fake data."""

    flush = True

    def handle(self, *args, **options):
        # self.stdout.write(self.style.NOTICE("** Populating Legionella DB "
        #                                     "with dummy data **"))

        create_players(self)
