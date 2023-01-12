from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    current_price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey(Category, related_name="listings")



class Bid(models.Model):
    pass

class Comment(models.Model):
    pass

class Watchlist(models.Model):
    pass

class Category:
    type = models.CharField(max_length=64)

# maybe one more model for categories -- categories, each with their own id