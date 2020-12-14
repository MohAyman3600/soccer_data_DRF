from django.contrib import admin
from django.contrib.admin.options import StackedInline
from api.models import League, Team, Player, Season, TeamStats, PlayerStats


class SeasonInline(admin.StackedInline):
    model = Season


class TeamStatsInline(admin.StackedInline):
    model = TeamStats


class PlayerStatsInline(admin.StackedInline):
    model = PlayerStats


class LeagueAdmin(admin.ModelAdmin):
    inlines = [SeasonInline, ]
    list_display = ('league_name', 'country_name', "league_logo")


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamStatsInline, ]
    list_display = ("team_name", "team_country",)


class PlayerAdmin(admin.ModelAdmin):
    inlines = [PlayerStatsInline, ]
    list_display = ("player_id", "player_name",)


admin.site.register(League, LeagueAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
