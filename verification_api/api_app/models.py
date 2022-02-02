from django.db import models

class WordleFeedback(models.Model):
  position_array = models.CharField(max_length=5)

