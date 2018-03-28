from django.urls import path
from .views import PrivateGraphQLView
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^graphql', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True))),
    path('', views.index, name='index'),
]
