from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length= 250)
	email =models.CharField(max_length=270)

class offers(models.Model):
	offer_Name = models.CharField(max_length=250)
	Description = models.CharField(max_length= 400)
	item = models.CharField(max_length=450)

class Partner(models.Model):
	Partener_company = models.CharField(max_length=250)
	Associted_person = models.CharField(max_length= 250)
	email =models.CharField(max_length=270)
	Phone_number =models.CharField(max_length=270)


