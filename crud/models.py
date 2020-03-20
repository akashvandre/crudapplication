from django.db import models

# Create your models here.

class Addmition(models.Model):
	am_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=70)
	email = models.CharField(max_length=70, default="")
	password = models.CharField(max_length=70)
	phone = models.CharField(max_length=12)
	wclass = models.CharField(max_length=50)
	stream = models.CharField(max_length=50)
	fees = models.IntegerField()
	pending_fees = models.IntegerField()
	dob = models.DateField()

	def __str__(self):
		return self.name

