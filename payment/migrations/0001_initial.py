# Generated by Django 2.2.7 on 2020-01-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='finalpayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(blank=True, max_length=255)),
                ('paymentclass', models.CharField(max_length=255)),
                ('paymentterm', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Paymentinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentclass', models.CharField(blank=True, max_length=255)),
                ('paymentterm', models.CharField(blank=True, max_length=255)),
                ('paymentamount', models.IntegerField(blank=True)),
            ],
        ),
    ]
