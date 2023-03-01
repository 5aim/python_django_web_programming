from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True) # 공백을 가질 수 있음.
    url = models.URLField('URL', unique=True) # 'URL' : verbose name - Admin site에서 보게 됨.

    # 객체를 문자열로 표현할 때 사용하는 함수.
    def __str__(self):
        return self.title