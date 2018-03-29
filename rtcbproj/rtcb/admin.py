from django.contrib import admin
from rtcb.tournament.models import Match
from rtcb.team.models import Team
from .authentication.models import User


admin.site.register(Team)
admin.site.register(Match)
admin.site.register(User)
