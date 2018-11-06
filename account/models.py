from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length= 250)
	email = models.EmailField()

class Partner(models.Model):
	Partener_company = models.CharField(max_length=250)
	Associted_person = models.CharField(max_length= 250)
	email = models.EmailField()
	Phone_number =models.CharField(max_length=270)

class offer(models.Model):

    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True)
    offer_Name = models.CharField(max_length=250)
    Description = models.CharField(max_length= 400)


class Discount(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    silver=models.CharField(max_length=250, default='')
    gold=models.CharField(max_length=250 , default='')
    platinum=models.CharField(max_length=250,default='')
    # level1 = models.IntegerField(default=0)
    # level2 = models.IntegerField(default=0)
    # level3 = models.IntegerField(default=0)
    # discount_per= models.IntegerField(default=0)

class Customer(models.Model):
    chasis_no = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    password= models.CharField(max_length=100)


class Promotion(models.Model):
    Partner = models.ForeignKey(Partner, on_delete=models.CASCADE , null=True)
    promotion_type = models.CharField(max_length=50, default='')
    image= models.ImageField(upload_to='profile_image', default='')
    description = models.TextField(max_length=1000, default='')

class Trasaction(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE , null=True)
    Partner = models.ForeignKey(Partner,on_delete=models.CASCADE)
    Discount = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)

