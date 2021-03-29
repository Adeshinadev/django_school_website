from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Paymentinfo(models.Model):
    paymentclass=models.CharField(max_length=255,blank=True)
    paymentterm=models.CharField(max_length=255,blank=True)
    paymentamount=models.IntegerField(blank=True)
    section = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.paymentclass


class finalpayment(models.Model):
    email=models.CharField(max_length=255,blank=True)
    reference_id=models.CharField(max_length=255,blank=True)
    paymentclass=models.CharField(max_length=255)
    paymentterm=models.CharField(max_length=255)
    paymentamount = models.IntegerField()
    date = models.CharField(max_length=255,blank=True)
    section = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.reference_id