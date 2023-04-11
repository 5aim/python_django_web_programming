from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html' # TemplateView를 사용할 경우 필수적으로 template_name을 지정해야 함.