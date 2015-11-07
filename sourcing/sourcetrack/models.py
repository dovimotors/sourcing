from django.db import models

# Create your models here.
class Interview(models.Model):
	int_date = models.DateTimeField('date interviewed')
	source = models.CharField(max_length=200)
	employee = models.CharField(max_length=50)