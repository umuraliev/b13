from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('title', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def str(self):
        return self.title


    def get_absolute_url(self):
        return reverse('services_list',
                       args=[self.slug, ])

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Barber(models.Model):
    category = models.ForeignKey(Category, related_name='cat_ber', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=55)
    description = models.TextField()
    image = models.ImageField(upload_to='media', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return f'{self.name}'


