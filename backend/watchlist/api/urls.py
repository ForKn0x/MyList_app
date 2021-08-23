from django.contrib import admin
from django.urls import path, include
from watchlist.api.views import WatchlistView, WatchlistDetailView, PlatformView, PlatformDetailView, ReviewView, ReviewDetailView

urlpatterns = [
    path('list/', WatchlistView.as_view()),
    path('list/<int:id>', WatchlistDetailView.as_view()),
    path('platform/', PlatformView.as_view()),
    path('platform/<int:id>', PlatformDetailView.as_view()),
    path('review/', ReviewView.as_view()),
    path('review/<int:id>', ReviewDetailView.as_view()),
]