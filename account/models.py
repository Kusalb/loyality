from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length= 250)
	email =models.CharField(max_length=270)

class offer(models.Model):
	offer_Name = models.CharField(max_length=250)
	Description = models.CharField(max_length= 400)


class Partner(models.Model):
	Partener_company = models.CharField(max_length=250)
	Associted_person = models.CharField(max_length= 250)
	email =models.CharField(max_length=270)
	Phone_number =models.CharField(max_length=270)

class DiscountAmount(models.Model):
    # silver=models.CharField(max_length=250)
    # gold=models.CharField(max_length=250)
    # platinum=models.CharField(max_length=250)
    level = models.IntegerField(default=1)
    discount_per= models.IntegerField(default=5)

class Customer(models.Model):
    chasis_no = models.CharField(max_length=200)
    c_id = models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')

class Promotion(models.Model):

    promotion_type = models.CharField(max_length=50, default='')
    image= models.ImageField(upload_to='profile_image', default='')
    description = models.TextField(max_length=1000, default='')

class Trasaction(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE , null=True)
    Partner = models.ForeignKey(Partner,on_delete=models.CASCADE)
    Discount = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)

