from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    #Example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),
    
    #Example: /photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),
    
    #Example: /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),
    
    #Example: /photo/photo/99/
    path('photo/<int:pK>/', views.PhotoDV.as_view(), name='photo_detail'),
]


# # 아래와 같은 경우 veiws.py를 작성하지 않아도 됨

# from django.urls import path
# from django.views.generic import ListView, DetailVeiw

# from photo.models import Album, Photo

# app_name = 'photo'
# urlpatterns = [
#     path('', ListView.as_view(model=Album), name='index'),
#     path('album/<int:pk>/', DetailVeiw.as_view(model=Album), name='album_detail'),
#     path('photo/<int:pk>/', DetailVeiw.as_view(model=Photo), name='photo_detail'),
# ]