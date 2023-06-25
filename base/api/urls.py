from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'artists', views.ArtistVS, basename='artist')
router.register(r'albums', views.AlbumModelVS, basename='album')

urlpatterns = [

    path('genres/', views.GenresList.as_view(), name="genres"),
    path('genres/<int:pk>/', views.GenreDetail.as_view(), name="genre-detail"),

    path('', include(router.urls)),
    path('songs/', views.SongsList.as_view(), name="songs"),
    path('song/<int:pk>', views.SongDetail.as_view(), name="song-detail"),
    path('playlist/', views.PlaylistView.as_view(), name='playlist'),
    path('playlist/<int:pk>/', views.PlaylistDetail.as_view(), name='playlist'),

]