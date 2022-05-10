from django.urls import reverse
from myaccount.models import MyUser
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation


# class LikeDislike(models.Model):
#     LIKE = 1
#     DISLIKE = -1
 
#     VOTES = (
#         (DISLIKE, 'Не нравится'),
#         (LIKE, 'Нравится')
#     )
 
#     vote = models.SmallIntegerField(verbose_name=("Голос"), choices=VOTES)
#     user = models.ForeignKey(MyUser, verbose_name=("Пользователь"))
 
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()
 
#     objects = LikeDislikeManager()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug, ])



class Product(models.Model):
    # votes = GenericRelation(LikeDislike, related_query_name='products')
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media', blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=0)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    
    def get_absolute_url(self):
        return reverse('product_details',
                        args=[self.slug, ])


    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


    def save(self):
        self.slug = self.name.lower().replace(" ", '-')
        return super().save()


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Comment by {} with email: {}'.format(self.name, self.email)


# class LikeDislike(models.Model):
#     LIKE = 1
#     DISLIKE = -1
 
#     VOTES = (
#         (DISLIKE, 'Не нравится'),
#         (LIKE, 'Нравится')
#     )
 
#     vote = models.SmallIntegerField(verbose_name=("Голос"), choices=VOTES)
#     user = models.ForeignKey(MyUser, verbose_name=("Пользователь"))
 
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey()
 
#     objects = LikeDislikeManager()