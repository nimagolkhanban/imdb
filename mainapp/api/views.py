from mainapp.models import WatchList, StreamPlatform, Review
from rest_framework import  status
from .serializers import WatchListSerializer, StreamPlatformSerializer, RevieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from mainapp.api.permissions import AdminOrReadOnly, ReviewUserReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class UserReview(generics.ListAPIView):
    serializer_class = RevieSerializer
    
    def get_queryset(self):
        username = self.kwargs["username"]
        return Review.objects.filter(review_user__username=username)
    
    # def get_queryset(self):
    #     username = self.request.query_params.get("username", None)
    #     if username :
    #         return Review.objects.filter(review_user__username=username)
    #     return Response("invalid username", status=status.HTTP_404_NOT_FOUND)
    #remember for this filtering method you should delete the username in url file 

class ReciewCreate(generics.CreateAPIView):
    serializer_class= RevieSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        movie = WatchList.objects.get(pk=pk)
        user = self.request.user
        review_user = Review.objects.filter(watchlist=movie, review_user= user)
        if review_user.exists():
            raise ValidationError("you can only submit one review in each movie")
        if movie.rating_count == 0:
            movie.avg_rating = serializer.validated_data["rating"]
        else:
            movie.avg_rating = (serializer.validated_data["rating"]+ movie.avg_rating)/2
        movie.rating_count +=1
        movie.save()
            
        serializer.save(watchlist=movie, review_user=user)
        
    

class ReviewList(generics.ListAPIView):
    serializer_class = RevieSerializer
    # permission_classes = [AdminOrReadOnly]
    throttle_classes = [AnonRateThrottle]
    
    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Review.objects.filter(watchlist=pk)
        
    
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = RevieSerializer
    permission_classes = [AdminOrReadOnly]
    


# class ReviewListAV(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = RevieSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
    
# class ReviewDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = RevieSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
        

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(instance= movies, many=True)
        
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchListDetailAV(APIView):
    
    def get(self, request, pk):
        try:
             movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"message":"there is no WatchList with this id"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = WatchListSerializer(instance=movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"message":"there is no WatchList with this id"}, status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(instance=movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"message":"there is no WatchList with this id"}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class StreamPlatformListAV(APIView):
    def get(self, request):
        stream_platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(instance= stream_platform, many=True)
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):
    
    def get(self, request, pk):
        try:
             stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"message":"there is no StreamPlatform with this id"}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = StreamPlatformSerializer(instance=stream_platform,context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"message":"there is no StreamPlatform with this id"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StreamPlatformSerializer(instance=stream_platform, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"message":"there is no StreamPlatform with this id"}, status=status.HTTP_404_NOT_FOUND)
        stream_platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





































# @api_view(["GET", "POST"])
# def movie_list(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(instance=movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# @api_view(["GET", 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"message":"there is no movie with this id"}, status=status.HTTP_404_NOT_FOUND)
            
#         serializer = MovieSerializer(instance=movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"message":"there is no movie with this id"}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(instance=movie, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"message":"there is no movie with this id"}, status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


