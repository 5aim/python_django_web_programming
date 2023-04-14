from django.db import models
from django.urls import reverse

# fields.py 사진에 대한 원본이미지와 썸네일 이미지를 모두 저장할 수 있는 필드. 직접 만든 커스텀 필드
from photo.fields import ThumbnailImageField


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
    # URL 반환. 장고 내장함수 reverse
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE', max_length=30)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m') # upload to 옵션으로 저장할 위치를 지정.
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True) # 객체가 생성될 때 자동으로 기록.
    
    class Meta:
        ordering = ('title',) # 객체 리스트를 출력할 때 title 컬럼을 기준으로 오름차순으로 정렬
        
    def __str__(self):
        return self.title
    
    # URL 반환
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))