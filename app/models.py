from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, default="error")
    author_first = models.CharField(max_length=50, blank=False, default="error")
    author_last = models.CharField(max_length=50, blank=False, default="error")
    cover_front = models.ImageField(blank=False, default=None, upload_to="covers/")
    cover_back = models.ImageField(blank=False, default=None, upload_to="covers/")
    summary = models.CharField(max_length=1000, blank=False, default=None)
    price = models.DecimalField(max_digits=4, decimal_places=2, blank=False, default=None)
    stars = models.DecimalField(max_digits=2, decimal_places=1, blank=False, default=None)
    views = models.IntegerField(blank=False, default=0)
    published = models.DateField(blank=False, default=None)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    star_choices = (("ONE", 1), ("TWO", 2), ("THREE", 3), ("FOUR", 4), ("FIVE", 5))
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, default=None)
    stars = models.IntegerField(choices=star_choices, blank=False, default=5)
    title = models.CharField(max_length=40, blank=False, default=None)
    content = models.CharField(max_length=1000, blank=False, default=None)