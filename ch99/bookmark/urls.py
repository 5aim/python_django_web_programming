from django.urls import path
from bookmark import views

app_name = 'bookmark' # app namespace : URL 패턴의 이름을 정하는데 사용. URL 패턴 이름이 충돌되지 않도록 함.

urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'), # URL 패턴의 이름은 bookmark를 포함해 index. bookmark:index가 됨.
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'), # bookmark:detail. 
    
    #Example: /bookmark/add/
    path('add/', views.BookmarkCreateView.as_view(), name="add"),
    
    #Example: /bookmark/change/
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),
    
    #Example: /bookmark/99/update/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),
    
    #Example: /bookmark/99/delete/
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),
]