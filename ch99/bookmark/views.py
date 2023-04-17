# class형 generic view를 사용하기 위해
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark  # 테이블 조회를 위해
from django.views.generic import CreateView, UpdateView, DeleteView # 편집용 제네릭 뷰
from django.contrib.auth.mixins import LoginRequiredMixin # @login_required() 로그인 X -> 리다이렉트
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin # 소유자만 행동

# Create your views here.
# 레코드 리스트를 보여주기 위해서 ListView를 상속받음. 객체가 들어있는 List를 구성해서 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 됨. 테이블에 모든 레코드를 가져와 구성하는 경우 테이블명, 즉 모델 클래스명만 지정해주면 됨.


class BookmarkLV(ListView):
    model = Bookmark

# 테이블에서 PK로 조회해서 특정 객체를 가져오는 경우 테이블명, 즉 모델 클래스명만 지정해주면 됨. urlconf에서 추출해 뷰로 넘어온 인자를 사용.


class BookmarkDV(DetailView):
    model = Bookmark


# 북마크 작성
class BookmarkCreateView(LoginRequiredMixin, CreateView): # 로그인 페이지로 이동 & 폼 에러 없으면 레코드 생성.
    model = Bookmark # 레코드 추가할 대상 테이블 설정
    fields = ['title', 'url'] # title, url 폼을 보여줌.
    success_url = reverse_lazy('bookmark:index') # 생성 완료된 후 이동할 URL
    
    def form_valid(self, form): # 유효성 검사
        form.instance.owner = self.request.user # 폼에 연결 모델 객체의 owner 필드에 현재 로그인된 user 할당.
        return super().form_valid(form) # form_valid 메소드에 의해 form.save() success_url redirect

# 북마크 리스트
class BookmarkChangeLV(LoginRequiredMixin, ListView): # ListVeiw 상속으로 객체의 리스트만 지정하면 그 리스트를 화면에 출력해 줌.
    template_name = 'bookmark/bookmark_change_list.html'
    
    # 화면에 출력할 레코드 리스트 반환. 로그인한 사용자가 소유한 콘텐츠만 보여짐.
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

# 북마크 업데이트
class BookmarkUpdateView(OwnerOnlyMixin, UpdateView): # 소유자가 아닌 경우 익셉션 처리해 줌.
    model = Bookmark # UpdateView 기능 적용 대상 테이블
    fields = ['title', 'url'] # UpdateView 기능 적용 대상 테이블의 레코드
    success_url = reverse_lazy('bookmark:index') # 내부적으로 form_valid() 호출. 레코드 수정 & 리다이렉트

# 북마크 삭제
class BookmarkDeleteView(OwnerOnlyMixin, DeleteView): # 기존 레코드 중 지정된 레코드를 삭제할 것인지 확인하는 페이지를 보여줌.
    model = Bookmark # DeleteView 기능 적용 대상 테이블
    success_url = reverse_lazy('bookmark:index') # 리다이렉트