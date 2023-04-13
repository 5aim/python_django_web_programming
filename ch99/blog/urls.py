from django.urls import path, re_path # 한글 슬러그를 위해 re_path()를 사용.
from blog import views # view class가 많아서 그냥 view 모듈 자체를 임포트해줌.

app_name = 'blog'
urlpatterns = [

    # Example: /blog/
    path('', views.PostLV.as_view(), name='index'),

    # Example: /blog/post/ (same as /blog/)
    path('post/', views.PostLV.as_view(), name='post_list'), # /blog/와 /blog/post/ 두가지 요청을 처리함을 주의.

    # Example: /blog/post/django-example/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), # slug converter
    # path('post/<slug:slug>/', views.PostDV.as_view(), name='post_detail'), # 이렇게 하면 한글이 포함된 슬러그는 처리 못함.

    # Example: /blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),

    # Example: /blog/archive/2019
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),

    # Example: /blog/archive/2019/nov
    path('archive/<int:year>/<str:month>', views.PostMAV.as_view(), name='post_month_archive'),

    # Example: /blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>', views.PostDAV.as_view(), name='post_day_archive'),
    
    # Example: /blog/archive/4자리 숫자/3자리 소문자/한두 자리 숫자/ = 정규식으로 표현
    # re_path(r'^archive/(?<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', views.PostDAV.as_view(), name='post_day_archive'),

    # Example: /blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
    
    #Example: /blog/tag/
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    
    #Example: /blog/tag/tagname/
    path('tag/<str:tag>', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    
    #Example: /blog/search/
    path('search/', views.SearchFormView.as_view(), name='search'),
]   