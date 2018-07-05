# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


ROLES = (
    ('', ''),
    ('D', 'Defender'),
    ('S', 'Striker')
)


# Custom User Model
class CustomUserManager(BaseUserManager):
    """ Modello personalizzato per la gestione degli utenti.
    """
    use_in_migrations = True

    # Metodo originale di django
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Metodo originale di django
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    # Metodo originale di django
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    """ Modello dell'utente custom.
    Lo defininiamo subito così, anche vuoto.
    Permette personalizzazioni future senza rompere niente o senza diventare
    matti ad incastrare la migrazione dei dati.
    """

    objects = CustomUserManager()

    def is_member(self, groupname):
        """ Questo metodo controlla se User fa parte del gruppo <groupname>.
        Restituisce True in caso positivo.
        """
        return self.groups.filter(name=groupname).exists()

    role = models.CharField(
        verbose_name="Primary role (favorite)",
        max_length=4,
        choices=ROLES,
        null=False,
        blank=False,
    )

    versatile = models.BooleanField(
        verbose_name="Can switch role?",
        default=False,
        help_text='This flag is selected if the player can also play '
                  'as the not favorite role.')
