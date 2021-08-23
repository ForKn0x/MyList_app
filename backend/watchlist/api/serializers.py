from watchlist.models import Watchlist, Platform
from rest_framework import serializers

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields ='__all__'

class PlatformSerializer(serializers.ModelSerializer):
    watchlist_platform = WatchlistSerializer(many=True, read_only=True)

    class Meta:
        model = Platform
        fields ='__all__'
