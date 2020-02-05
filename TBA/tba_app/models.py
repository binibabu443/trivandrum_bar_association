from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=30)
    mobileno=models.CharField(max_length=50)
    emailid=models.EmailField()
    types=models.CharField(max_length=30)
    officeadd=models.CharField(max_length=50)
    residenceadd=models.CharField(max_length=50)
    joiningdate=models.DateField()
    duration=models.CharField(max_length=20)
    approvedate=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    expirydate=models.DateField(null=True,blank=True)

    class meta:
        db_table="registration"

class admin(models.Model):
    emailid=models.EmailField()
    password=models.CharField(max_length=50)

class contact(models.Model):
    name=models.CharField(max_length=30)
    emailid=models.EmailField()
    subject=models.CharField(max_length=30)
    msg=models.CharField(max_length=50)
    status=models.CharField(max_length=10,null=True,blank=True,default='off')


    class meta:
        db_table="contact"