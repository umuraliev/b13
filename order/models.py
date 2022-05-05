from django.db import models
from account.models import User


class Order(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




