from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark) # 데코레이터를 사용하여 어드민 사이트에 등록.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# # register()를 사용해서 아래와 같이도 작성가능
# admin.site.register(Bookmark, BookmarkAdmin)