#Nichole Booker 4-3-2026

from django.db import models

# Create your models here.
class Item(models.Model):
	text = models.TextField(default="")
