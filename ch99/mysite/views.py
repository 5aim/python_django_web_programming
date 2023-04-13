from django.views.generic import TemplateView

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Homepage view
class HomeView(TemplateView):
    template_name = 'home.html' # TemplateView를 사용할 경우 필수적으로 template_name을 지정해야 함.


# User creation
class UserCreateView(CreateView):
    templates_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')
    
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'