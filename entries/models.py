from django.db import models
from account.models import User
from service.models import Category

class Entries(models.Model):
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)