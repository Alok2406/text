from django.db import models

# Create your models here.

class ReversedText(models.Model):
    original_text = models.CharField(max_length=200)
    reversed_text = models.CharField(max_length=200)
