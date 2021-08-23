from watchlist.models import Watchlist, Platform, Review
from rest_framework import generics
from .serializers import WatchlistSerializer, PlatformSerializer, ReviewsSerializer
from watchlist.models import Watchlist, Platform
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .permissions import IsAdminOrReadOnly, IsReviewerOrReadOnly

class WatchlistView(generics.ListCreateAPIView):
        queryset = Watchlist.objects.all()
        serializer_class = WatchlistSerializer

class WatchlistDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Watchlist.objects.all()
        serializer_class = WatchlistSerializer
        lookup_field = 'id'

class PlatformView(generics.ListCreateAPIView):
        queryset = Platform.objects.all()
        serializer_class = PlatformSerializer

class PlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Platform.objects.all()
        serializer_class = PlatformSerializer
        lookup_field = 'id'

class ReviewView(generics.ListAPIView):
        #queryset = Review.objects.all()
        serializer_class = ReviewsSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]

        def get_queryset(self):
            pk = self.kwargs['id']
            return Review.objects.filter(watchlist = pk)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Review.objects.all()
        serializer_class = ReviewsSerializer
        permission_classes = [IsReviewerOrReadOnly]
        lookup_field = 'id'

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['id']
        item = Watchlist.objects.get(pk = pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist = item, review_user = review_user)

        if review_queryset.exists():
                raise ValidationError("Already have one review")

        serializer.save(watchlist = item, review_user = review_user)


##################################### The portion below does the same thing as above using mixins ##################################

# class WatchlistView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#     queryset = Watchlist.objects.all()
#     serializer_class = WatchlistSerializer

#     lookup_field = 'id'

#     def get(self, request, id = None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id):
#         return self.update(request, id)

# class PlatformView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#     queryset = Platform.objects.all()
#     serializer_class = PlatformSerializer

#     lookup_field = 'id'

#     def get(self, request, id = None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id):
#         return self.update(request, id)


# class ReviewView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
#     queryset = Review.objects.all()
#     serializer_class = ReviewsSerializer

#     lookup_field = 'id'

#     def get(self, request, id = None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request, id)

#     def delete(self, request, id):
#         return self.destroy(request, id)

#     def post(self, request):
#         return self.create(request)

#     def put(self, request, id):
#         return self.update(request, id)