from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from .views import PrivateGraphQLView


urlpatterns = [
    url(r'^graphql', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True))),
    url(r'^refresh-token', refresh_jwt_token),
    url(r'^login', obtain_jwt_token),
]
