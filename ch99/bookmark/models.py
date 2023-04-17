from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True) # 공백을 가질 수 있음.
    url = models.URLField('URL', unique=True) # 'URL' : verbose name - Admin site에서 보게 됨.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # 객체를 문자열로 표현할 때 사용하는 함수.
    def __str__(self):
        return self.title