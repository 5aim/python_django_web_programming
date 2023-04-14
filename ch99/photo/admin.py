from django.contrib import admin
from photo.models import Album, Photo

# Register your models here.
class PhotoInline(admin.StackedInline): # 1:N 세로로 나열. & TabularInline
    model = Photo # 추가로 보여지는 photo table
    extra = 2 # 이미 존재하는 객체 외 추가로 입력할 수 있는 photo 테이블 객체의 수는 2개


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,) # 앨범객체 수정화면 photoinline 클래스를 정의한 사항을 같이 보여줌.
    list_display = ('id', 'name', 'description')


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_dt')