from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import DestroyAPIView,ListAPIView
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from .models import Video
from .video_player import VideoPlayer
import threading


# this view helps the user to upload a new video
class UploadVideoView(APIView):
    permission_classes  = [IsAuthenticated]
    def post(self,request):
        data            = request.data
        serialized_data = VideoSerializer(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response({'upload_success':'video uploaded successfully'},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serialized_data.errors},status=status.HTTP_400_BAD_REQUEST)


# this view helps to play each videos on independent thread
class PlayVideoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,video_id):
        video          = Video.objects.get(id=video_id)
        video_player   = VideoPlayer(video.video_URL.path)
        thread         = threading.Thread(target=video_player.play_video)
        thread.daemon  = True
        thread.start()
        return Response({'playing':'video is successfully playing in the background'})


# this view function helps to update an existing video
class UpdateVideoView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,video_id):
        data           = request.data
        video          = Video.objects.get(id=video_id)
        serializer     = VideoSerializer(video,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'update successfull'},status=status.HTTP_200_OK)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


# this view helps user to delete a video   
class DestroyVideoView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset           = Video.objects.all()
    lookup_field       = 'id'


# This view helps in the search functionality
class SearchVideoView(APIView):
    permission_classes    = [IsAuthenticated]
    def get(self,request):
        search_query      = request.query_params.get('search_query','')
        videos            = Video.objects.filter(title__icontains=search_query)
        serialized_output = VideoSerializer(videos,many=True)
        return Response(serialized_output.data,status=status.HTTP_200_OK)


# a custom pagination class to handle pagination
class CusotmPagination(PageNumberPagination):
    page_size             = 10
    page_size_query_param = 'page_size'
    max_page_size         = 50


# this view helps to fetch all of the videos from database
class FetchAllVideosView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset           = Video.objects.all()
    serializer_class   = VideoSerializer
    pagination_class   = CusotmPagination

        


