from django.db import models
from django.utils import timezone
# Create your models here.
class posts(models.Model):
	autor = models.CharField(max_length=20)
	title = models.CharField(max_length=200)
