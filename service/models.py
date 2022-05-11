from django.db import models
from django.urls import reverse
from myaccount.models import MyUser



class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField()


    class Meta:
        ordering = ('title', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
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

    class Meta:
        verbose_name = 'барбер'
        verbose_name_plural = 'барберы'

    def __str__(self):
        return f'{self.name} {self.last_name}'




class EntriesTime(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='entruser')
    date = models.DateField()
    time = models.TimeField()





