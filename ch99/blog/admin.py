from django.contrib import admin
from blog.models import Post

@admin.register(Post) # admin.site.register()를 사용해도 됨.
class PostAdmin(admin.ModelAdmin): # 포스트가 admin에서 어떤 모습으로 보여줄지 정의
    list_display = ('id', 'title', 'modify_dt') # post 객체 보여줄 때
    list_filter = ('modify_dt',) # 필터 사이드바를 보여주도록 지정
    search_fields = ('title', 'content') # 검색박스 표시
    prepopulated_fields = {'slug': ('title',)} # slug필드는 title필드를 사용해 미리 채워지도록
