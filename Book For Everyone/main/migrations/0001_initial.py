# Generated by Django 3.0 on 2020-11-29 07:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('author', models.CharField(default='', max_length=20)),
                ('publication', models.CharField(default='', max_length=30)),
                ('name', models.CharField(default='', max_length=15)),
                ('phone_no', phonenumber_field.modelfields.PhoneNumberField(default='+91 ', max_length=128, region=None)),
                ('email', models.EmailField(default='', max_length=254)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
