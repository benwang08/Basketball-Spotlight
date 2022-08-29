from distutils.command.build_scripts import first_line_re
from django.db import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    teams = (
        (1, "Hawks"),
    )
    team_id = models.IntegerField(choices=teams, default=-1)

class Player(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    nba_api_id = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name + " - " + self.team.get_team_id_display()



class User(AbstractUser):

    team = models.OneToOneField(Team, blank=True, null=True, on_delete=models.CASCADE)
    player1 = models.OneToOneField(Player, related_name="player1", blank=True, null=True, on_delete=models.CASCADE)
    player2 = models.OneToOneField(Player, related_name="player2", blank=True, null=True, on_delete=models.CASCADE)
    player3 = models.OneToOneField(Player, related_name="player3", blank=True, null=True, on_delete=models.CASCADE)



