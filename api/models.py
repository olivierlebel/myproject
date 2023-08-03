from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'players'

