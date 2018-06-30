# -*- coding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView


# Create your views here.
def index(request):
    return HttpResponse("<h1>RedTurtle Calcio Balilla!</h1>")


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    raise_exception = True


class SiteRoot(TemplateView):
    template_name = "index.html"
