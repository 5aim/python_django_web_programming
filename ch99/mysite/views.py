from django.views.generic import TemplateView

from django.views.generic import CreateView # 편집용 제네릭뷰
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy # URL 패텀명을 받음. 작성하고 있는 views.py 모듈이 로딩되고 처리되는 시점에 urls가 작동되지 않을 수 있으므로 reverse대신 reverse lazy를 사용

from django.contrib.auth.mixins import AccessMixin # 권한을 갖췄는지 판단

# Homepage view
class HomeView(TemplateView):
    template_name = 'home.html' # TemplateView를 사용할 경우 필수적으로 template_name을 지정해야 함.


# User creation
class UserCreateView(CreateView): # /accounts/register/ URL을 처리하는 뷰. 폼에 입력된 내용에서 에러 여부 체크해 줌.
    template_name = 'registration/register.html' # 화면에 보여줄 템플릿 이름. 다음 줄 form class 속성에 지정된 폼 사용.
    form_class = UserCreationForm # 장고의 기본 폼 사용.
    success_url = reverse_lazy('register_done') # 테이블 레코드 생성이 완료된 후에 이동할 URL 지정. /accounts/register/done/

# /accounts/register/done/을 처리해줌. 특별로직없이 템플릿만 보여주면 됨.    
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'


# mixin 클래스 추가
class OwnerOnlyMixin(AccessMixin):
    raise_exception = True # 소유자가 아닌 경우 403처리 & 아래 메세지. False : 로그인페이지 리다이렉트
    permission_denied_message = "Owner only can update/delete the object"
    
    def dispatch(self, request, *args, **kwargs): # get 처리 이전 단계 dispatch 오버리아딩. 여기서 소유자 여부 판단. AccessMixin -> dispatch()
        obj = self.get_object() # 현재 대상이 되는 객체
        if request.user != obj.owner: # 403
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)