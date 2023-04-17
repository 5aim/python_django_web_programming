from django.db import models
from django.urls import reverse # URL 패턴을 만들어주는 장고의 내장 함수
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=100)
    # verbose name : 별칭. 폼화면에서 레이블로 사용되는 문구. Admin site 확인.
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    # 제목의 별칭. unique key로 특정 포스트 검색시 기본키 대신 사용. p.75
    # allow_unicode : 한글 처리가 가능하게
    # help text : 해달 컬럼을 설명해주는 문구로 폼화면에 나타남. Admin site 확인
    description = models.CharField('DESCRIPTION', max_length=200, blank=True, help_text='simple description text.')
    # blank true : 빈칸 설명도 가능
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    # auto now add : 객체가 생성되면 자동으로 시간을 기록
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    # auto now : 데이터베이스에 저장될 때 시간을 기록.
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)

    class Meta:
        verbose_name = 'post' # 테이블 단수 별칭
        verbose_name_plural = 'posts' # 테이블 복수 별칭
        db_table = 'blog_posts' # default : 앱이름_모델클래스명. 즉 blog_post가 됨.
        ordering = ('-modify_dt',) # 모델 객체 출력시 내림차순 정렬

    def __str__(self):
        return self.title
    
    # 정의된 객체를 지칭하는 URL을 반환함. 메소드 내에서는 장고의 내장함수인 reverse()를 호출함.
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
    
    # 장고 내장함수. 최신 포스트를 먼저 보여주므로 get_previous_by_modify_df함수는 modify_dt기준으로 최신 포스트를 반환함.
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    # -modify_dt 기준으로 그 다음 포스트를 반환. 위와 동일. modify_dt를 기준으로 예전 포스트를 반환함.
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    # slug 필드를 자동으로 채워줌.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True) # allow_unicode 한글 처리 가능
        super().save(*args, **kwargs)