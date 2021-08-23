from django.contrib import admin
from django.urls import path, include
from watchlist.api.views import WatchlistView, WatchlistDetailView, PlatformView, PlatformDetailView, ReviewView, ReviewDetailView, ReviewCreateView

urlpatterns = [

    # Watchlist URLS
    path('list/', WatchlistView.as_view()),
    path('list/<int:id>', WatchlistDetailView.as_view()),

    # Platform URLS
    path('platform/', PlatformView.as_view()),
    path('platform/<int:id>', PlatformDetailView.as_view()),

    # Reviews URLS
    path('list/<int:id>/review-create', ReviewCreateView.as_view()),
    path('list/<int:id>/review/', ReviewView.as_view()),
    path('list/review/<int:id>', ReviewDetailView.as_view()),
]