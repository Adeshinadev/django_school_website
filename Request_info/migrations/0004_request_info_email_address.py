# Generated by Django 2.2.7 on 2020-02-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Request_info', '0003_remove_request_info_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='request_info',
            name='Email_address',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
    ]
