from django.db import models

# Create your models here.
class event(models.Model):
    date=models.CharField(max_length=255)
    month=models.CharField(max_length=255)
    main_content=models.TextField(max_length=255)

    def __str__(self):
        return self.date


class latest_news(models.Model):
    headline=models.CharField(max_length=255)
    date=models.DateField()
    new_content=models.CharField(max_length=500)
    content_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.headline
