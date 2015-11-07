from django.db import models

# Create your models here.
class Interview(models.Model):
	int_date = models.DateField(auto_now_add=True)
	source = models.CharField(max_length=200)
	employee = models.CharField(max_length=50)
	def __str__(self):
		return self.source