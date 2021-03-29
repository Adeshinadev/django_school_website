from django.db import models

# Create your models here.
class Request_info(models.Model):
    Email_address=models.CharField(max_length=255)
    Name=models.CharField(max_length=255)
    Subject=models.CharField(max_length=255)
    Question=models.CharField(max_length=1000)

    def __str__(self):
        return self.Email_address
