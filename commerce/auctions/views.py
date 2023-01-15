from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    current_listings = Listing.objects.all()
    return render(request, "auctions/index.html", {"current_listings": current_listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing(request):
    if request.method == "POST":
        #TODO: create the forms for this page server side, then we can validate the information by the server (not just by the client)
        owner = request.user.username
        title = request.POST["title"]
        starting_price = request.POST["price"]
        description = request.POST["description"]
        image = "none"
        if request.POST["image"] != "":
            image = request.POST["image"]
        category = Category.objects.get(type="type")
        # send it to the database
        Listing.objects.create(
            title = title,
            current_price = starting_price,
            description = description,
            image = image,
            category = category,
            owner = request.user,
        )
        return HttpResponseRedirect(reverse("index"))

            
    else:
        return render(request, "auctions/create_listing.html")

def create_category(request):
    # make a category form in django, grab taht data from here and make a new category, then send the user back to the craete_listing page with there old form data
    pass

def display_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, "auctions/display_listing.html", {"listing":listing})

def watchlist(request, listing_id):
    if request.method == "POST":
        user = request.user
        watchlist_listing = Listing.objects.get(id=listing_id)
        Watchlist.objects.create(
            owner = user,
            listing = watchlist_listing
        )
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "auctions/watchlist.html", {"watchlists": Watchlist.objects.all()})