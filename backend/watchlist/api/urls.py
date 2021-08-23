from django.contrib import admin
from django.urls import path, include
from watchlist.api.views import WatchlistView, PlatformView, ReviewView

urlpatterns = [
    path('list/', WatchlistView.as_view()),
    path('list/<int:id>', WatchlistView.as_view()),
    path('platform/', PlatformView.as_view()),
    path('platform/<int:id>', PlatformView.as_view()),
    path('review/', ReviewView.as_view()),
    path('review/<int:id>', ReviewView.as_view()),
]