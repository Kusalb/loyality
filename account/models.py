from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length= 250)
	email =models.CharField(max_length=270)

class offer(models.Model):
	offer_Name = models.CharField(max_length=250)
	Description = models.CharField(max_length= 400)
	item = models.CharField(max_length=450)

class Partner(models.Model):
	Partener_company = models.CharField(max_length=250)
	Associted_person = models.CharField(max_length= 250)
	email =models.CharField(max_length=270)
	Phone_number =models.CharField(max_length=270)

class DiscountAmount(models.Model):
    # silver=models.CharField(max_length=250)
    # gold=models.CharField(max_length=250)
    # platinum=models.CharField(max_length=250)
    level1 = models.IntegerField(default=0)
    level2 = models.IntegerField(default=0)
    level3 = models.IntegerField(default=0)
    discount_per= models.IntegerField(default=0)

class CustomerInfo(models.Model):
    chasis_no = models.IntegerField( default=0)
    c_id = models.CharField(max_length=100, blank=False)
    password= models.CharField(max_length=100)
    fname = models.CharField(max_length=50, default='')
    lname = models.CharField(max_length=50, default='')

class Promotions(models.Model):

    promotion_type = models.CharField(max_length=50, default='')
    image= models.ImageField(upload_to='profile_image', blank=False, default='')
    description = models.TextField(max_length=1000, blank=False, default='')

class Trasaction(models.Model):
    CustomerInfo = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE , null=True)
    Partner = models.ForeignKey(Partner,on_delete=models.CASCADE)
    Discount = models.CharField(max_length=100)
    Total = models.CharField(max_length=100)

