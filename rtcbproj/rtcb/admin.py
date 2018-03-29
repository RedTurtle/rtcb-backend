from django.contrib import admin
from rtcb.tournament.models import Match, Tournament
from rtcb.team.models import Team
from .authentication.models import User


admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(User)
