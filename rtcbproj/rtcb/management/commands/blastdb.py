# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = """Questo comando permette di eliminare il dp sqlite3 e tutti i
    file di migrazione della app 'rtcb'.
    """

    flush = True

    def handle(self, *args, **options):
        print("\n\n")
        DB = settings.DATABASES['default']
        dbpath = DB['NAME']
        print("Deleting db: {}".format(dbpath))
        try:
            os.remove(dbpath)
        except FileNotFoundError:
            print(">> db not found.")
        os.chdir(settings.BASE_DIR)
        os.chdir(os.path.join('rtcb', 'migrations'))

        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                if name.startswith('000'):
                    # We removed .py and .pyc files
                    joinedpath = os.path.join(root, name)
                    print("Deleting file: {}".format(joinedpath))
                    try:
                        os.remove(joinedpath)
                    except FileNotFoundError:
                        print(">> Error: File not removed.")

        print("\n\tAll good.")
        print("\tNow you can run:\n")
        print("python manage.py makemigrations")
        print("python manage.py migrate\n\n")
        print("python manage.py createsuperuser\n\n")
