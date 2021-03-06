# Generated by Django 3.1.4 on 2021-01-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20210113_1848'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
