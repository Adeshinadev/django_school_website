# Generated by Django 2.2.7 on 2020-02-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email_address', models.EmailField(max_length=254)),
                ('Name', models.CharField(max_length=255)),
                ('Subject', models.CharField(max_length=255)),
                ('Question', models.CharField(max_length=1000)),
            ],
        ),
    ]
