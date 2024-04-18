from django.urls import path
from .views import (UploadVideoView,PlayVideoView,UpdateVideoView,DestroyVideoView,SearchVideoView,FetchAllVideosView)

urlpatterns = [
    path('uploadvideo/',UploadVideoView.as_view(),name='upload_video'),
    path('playvideo/<int:video_id>/',PlayVideoView.as_view(),name='play_video'),
    path('updatevideo/<int:video_id>/',UpdateVideoView.as_view(),name='update_video'),
    path('deletevideo/<int:id>/',DestroyVideoView.as_view(),name='delete_video'),
    path('search/',SearchVideoView.as_view(),name='search_video'),
    path('fetchallvideos/',FetchAllVideosView.as_view(),name='fetch_all_videos')  
]   