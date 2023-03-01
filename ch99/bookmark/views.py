from django.views.generic import ListView, DetailView # class형 generic view를 사용하기 위해
from bookmark.models import Bookmark # 테이블 조회를 위해

# Create your views here.
# 레코드 리스트를 보여주기 위해서 ListView를 상속받음. 객체가 들어있는 List를 구성해서 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 됨. 테이블에 모든 레코드를 가져와 구성하는 경우 테이블명, 즉 모델 클래스명만 지정해주면 됨.
class BookmarkLV(ListView):
    model = Bookmark

# 테이블에서 PK로 조회해서 특정 객체를 가져오는 경우 테이블명, 즉 모델 클래스명만 지정해주면 됨. urlconf에서 추출해 뷰로 넘어온 인자를 사용.
class BookmarkDV(DetailView):
    model = Bookmark