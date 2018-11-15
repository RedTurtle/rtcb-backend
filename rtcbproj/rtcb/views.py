# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from rtcb.team.models import Team
from rtcb.tournament.models import Tournament
from rtcb.authentication.models import User


def getTeams():
    return Team.objects.all()


def getTournaments():
    return Tournament.objects.all()


def getUsers():
    return User.objects.all()


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    raise_exception = True


class SiteRoot(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(SiteRoot, self).get_context_data(**kwargs)

        context['teams'] = getTeams()
        context['users'] = getUsers()
        context['tournaments'] = getTournaments()

        return context
