from django.contrib import admin # 필요한 모듈과 함수 import
from django.urls import path, include

# from bookmark.views import BookmarkLV, BookmarkDV # view 모듈 관련 class import
# from bookmark.views import * # 권장하지 않는 방식임. 불필요한 view를 import해서 충돌할 가능성 있음.

# 간단한 class형 view의 경우 views.py에 코딩할 필요 없이 URLconf에서 뷰 및 뷰 처리에 필요한 파라미터를 모두 지정할 수 있음. 아래와 같이 작성함.
# from django.views.generic import ListView, DetailView
# path('bookmark/', Listview.as_view(model=Bookmark), name='index'),
# path('bookmark/<int:pk>/', DetailView.as_view(model=Bookmark), name='detail'),

urlpatterns = [ # path()함수는 route, view 2개의 필수 인자. kwargs, name 2개의 선택 인자를 받음. name 인자는 templates file에서 많이 사용됨.
    path('admin/', admin.site.urls), # admin site 정의.
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),

    # class-based views
    # path('bookmark/', BookmarkLV.as_view(), name='index'), # URL 패턴의 이름은 index
    # path('bookmark/<int:pk>', BookmarkDV.as_view(), name='detail'), # URL 패턴의 이름은 detail
]
