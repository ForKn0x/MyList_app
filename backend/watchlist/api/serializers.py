from watchlist.models import Watchlist, Platform, Review
from rest_framework import serializers

class ReviewsSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields ='__all__'
        exclude = ('watchlist', )

class WatchlistSerializer(serializers.ModelSerializer):
    watchlist_reviews = ReviewsSerializer(many = True, read_only = True)

    class Meta:
        model = Watchlist
        fields ='__all__'

class PlatformSerializer(serializers.ModelSerializer):
    watchlist_platform = WatchlistSerializer(many=True, read_only=True)

    class Meta:
        model = Platform
        fields ='__all__'
