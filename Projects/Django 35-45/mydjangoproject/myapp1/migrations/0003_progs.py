# Generated by Django 5.0.1 on 2024-03-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_salesorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=35)),
                ('age', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=35)),
            ],
        ),
    ]