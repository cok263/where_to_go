# Generated by Django 3.1.4 on 2020-12-23 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20201223_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='imgs', to='places.place'),
        ),
    ]
