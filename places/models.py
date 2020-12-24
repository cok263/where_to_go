from django.db import models


class Place(models.Model):
    title = models.CharField("Название проекта", max_length=200, db_index=True)
    description_short = models.CharField("Краткое описание", max_length=250, db_index=True)
    description_long = models.TextField("Полное описание", blank=True)
    lat = models.FloatField('Широта')
    lng = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField('Изображение проекта', upload_to='images', null=True, blank=True)
    place = models.ForeignKey(
        'Place',
        related_name = 'imgs',
        on_delete=models.CASCADE,
        blank=True, null=True,
    )


    def __str__(self):
        return '{} {}'.format(self.id, self.place.title)
