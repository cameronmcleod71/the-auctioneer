from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("id=<int:listing_id>", views.display_listing, name="listing"),
    path("watchlist=<int:listing_id>", views.watchlist, name="watchlist"),
    path("category", views.category, name="category")
]
