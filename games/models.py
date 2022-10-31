from django.db import models


class BoardGame(models.Model):
    """Board game objet."""
    name = models.CharField(max_length=100)
    slug_name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    year = models.IntegerField()
