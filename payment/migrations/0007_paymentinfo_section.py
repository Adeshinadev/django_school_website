# Generated by Django 2.2.7 on 2020-01-25 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20200125_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinfo',
            name='section',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]