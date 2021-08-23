from watchlist.models import Watchlist, Platform, Review
from rest_framework import generics, mixins
from .serializers import WatchlistSerializer, PlatformSerializer, ReviewsSerializer
from watchlist.models import Watchlist, Platform

class WatchlistView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

class PlatformView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)


class ReviewView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)