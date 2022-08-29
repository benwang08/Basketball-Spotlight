from django.contrib import admin

# Register your models here.

from .models import User, Player, Team

admin.site.register(User)
admin.site.register(Player)
admin.site.register(Team)