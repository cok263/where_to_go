# Generated by Django 3.1.4 on 2021-01-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20210113_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveIntegerField(db_index=True, default=0, null=True),
        ),
    ]
