from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    type = models.CharField(max_length=64)

class Listing(models.Model):
    title = models.CharField(max_length=64)
    current_price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()
    image = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="listings")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_listings")

class Bid(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=12)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_bids")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()

class Watchlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_watchlist")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchers")



# maybe one more model for categories -- categories, each with their own id