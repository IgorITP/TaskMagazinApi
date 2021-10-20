# Generated by Django 3.1 on 2021-10-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Name Product')),
                ('price', models.CharField(default='', max_length=100, verbose_name='Price')),
                ('description', models.CharField(default='', max_length=100, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Price',
            },
        ),
    ]