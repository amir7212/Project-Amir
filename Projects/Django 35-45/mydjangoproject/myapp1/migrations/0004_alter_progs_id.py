# Generated by Django 5.0.1 on 2024-03-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0003_progs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progs',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
