from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Название проекта", max_length=200, db_index=True)
    description_short = models.CharField("Краткое описание", max_length=250, db_index=True)
    description_long = HTMLField("Полное описание", blank=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return "{} {}".format(self.id, self.title)


class Image(models.Model):
    image = models.ImageField('Изображение проекта', upload_to='images', null=True)
    number = models.PositiveIntegerField(default=0)
    place = models.ForeignKey(
        'Place',
        related_name = 'imgs',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ['number']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return '{} {}'.format(self.id, self.place.title)
