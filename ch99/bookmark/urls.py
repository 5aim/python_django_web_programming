from django.urls import path
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark' # app namespace : URL 패턴의 이름을 정하는데 사용. URL 패턴 이름이 충돌되지 않도록 함.

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'), # URL 패턴의 이름은 bookmark를 포함해 index. bookmark:index가 됨.
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'), # bookmark:detail. 
]