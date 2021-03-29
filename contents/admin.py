from django.contrib import admin
from .models import event,latest_news
# Register your models here.
admin.site.register(event)
admin.site.register(latest_news)