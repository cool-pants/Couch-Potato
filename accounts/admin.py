from django.contrib import admin

# Register your models here.

from .models import Member, Tournament, Game, Tier, Profile, Team, TeamMembers

admin.site.register(Game)
admin.site.register(Tier)
admin.site.register(Member)
admin.site.register(Tournament)
admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(TeamMembers)