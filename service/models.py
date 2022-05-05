from django.db import models

class Barber(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=55)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}'



