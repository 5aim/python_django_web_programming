# class generic view 임포트
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.conf import settings

# 테이블 조회를 위해 Post 모델 임포트
from blog.models import Post


# Create your views here.

#--- ListView
# ListView generic view : 테이블로부터 객체 리스트를 가져와 그 리스트를 출력해줌.
class PostLV(ListView):
    model = Post # 대상 테이블
    template_name = 'blog/post_all.html' # 템플릿 지정. 디폴트 : blog/post_list.html이 됨.
    context_object_name = 'posts' # 템플릿으로 넘겨주는 객체 리스트에 대한 컨텍스트 변수명 지정. 디폴트 : object_list
    paginate_by = 2 # 한페이지에 보여주는 객체 리스트의 숫자는 2. 장고 제공 페이징 기능 사용. 페이징 기능이 활성화되면 객체 리스트 하단에 페이지를 이동할 수 있는 버튼을 만들 수 있음.

#--- DetailView
# DetailView generic view : 테이블로부터 특정 객체를 가져와 그 객체의 상세 정보를 출력함. 테이블에서 특정 객체를 조회하기 위한 키는 기본 키 대신 slug 속성을 사용하므로 이 slug 파라미터는 URLconf에서 추출해 view로 넘겨줌.
class PostDV(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        # 기존 context 변수를 구하고 이를 context 변수에 할당.
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

#--- ArchiveView
# Archive generic view : 테이블에서부터 객체 리스트를 가져와서 날짜 필드를 기준으로 최신 객체를 먼저 출력.
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt' # 기준이 되는 날짜 필드는 modify_dt, 변경 날짜가 최신인 포스트를 먼저 출력한다는 것.

# YearArchiveView generic view : 테이블로부터 날짜 필드의 연도를 기준으로 객체 리스트를 가져와 그 객체들이 속한 월을 리스트로 출력. 날짜 필드의 연도 파라미터는 URLconf에서 추출해 view로 넘겨줌.
class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt' # 기준이 되는 날짜 필드는 modify_dt 컬럼 사용. 변경 날짜가 yyyy연도인 포스트를 검색해 그 포스트들의 변경 월을 출력함.
    make_object_list = True # 해당 연도에 해당하는 객체 리스트를 만들어서 템플릿으로 넘겨줌. 즉 템플릿 파일에서 object_list 컨텍스트 변수를 사용할 수 있고 디폴트는 False
    #month_format = '%b'

# MonthArchiveView generic view : 테이블로부터 날짜 필드의 연월을 기준으로 객체 리스트를 가져와 그 리스트를 출력. 날짜 필드의 연 월 파라미터는 URLconf에서 추출해서 view로 넘김.
class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt' # 날짜의 변경을 연 월을 기준으로 포스트를 검색해 그 포스트의 리스트를 출력.

# DayArchiveView generic view : 테이블로부터 날짜 필드의 연월일을 기준으로 객체 리스트를 가져와 그 리스트를 출력함. 날짜 필드의 연 월 일 파라미터는 URLconf에서 추출해 view로 넘김.
class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

# TodayArchiveView generic view : 테이블로부터 날짜 필드가 오늘인 객체 리스트를 출력함. 오늘 날짜를 기준 연월일로 지정한다는 점 외에는 DayArchiveView와 동일함.
class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt' # 변경 날짜가 오늘인 포스트를 검색. 그 포스트의 리스트 출력.
    
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'
    # 클라우드 처리 기능이 뷰에 있지 않고 taggit_cloud.html에 {% get_tagcloud %}로 처리.

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 상위 클래스의 컨텍스트 변수, 즉 변경 전의 컨텍스트 변수를 구함.
        context['tagname'] = self.kwargs['tag']
        # 추가할 컨텍스트 변수명은 tagname. URL에서 tag파라미터로 넘어온 값을 사용.
        # path('tag/<str:tag>', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
        return context
        # 컨텍스트 변수들이 템플릿 파일로 전달됨.