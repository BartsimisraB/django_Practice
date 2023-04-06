from django.urls import path
from . import views

# 경로 설정

urlpatterns = [
    path('li/', views.li, name='li'),
    # path('create/', views.create, name='create'),
    # name을 templates에서 지정한 action의 url 사용 가능
    # path 함수에 들어가는 name은 생략 (참조) 가능
    path('create/', views.create, name='res-create'),
    path('update/', views.update, name='res-update'),
    path('delete/', views.delete, name='res-delete'),
    # path('read/<int:id>/', views.read, name='res-read'), # <int:id> : 파라미터
    # three/food/게시글 번호 매핑 - read 함수와 연관
    path('food/<int:id>/', views.read, name='res-read'), # <int:id> : 파라미터
    # 지정한 url으로 매서드를 실행시킨 후 보내겠다는 의미 >> 진입시 url과는 다른 의미
    path('review_create/<int:food_id>/review/create/', views.review_create, name='review_create'),
    path('review_delete/<int:food_id>/review/delete/<int:review_id>/', views.review_delete, name='review_delete'),
]

# 경로명, 함수, 이름
# 우리가 실행하는 파일 자체는 views.메서드 가 실행되는 것.
# name은 url 형태로들어갈 수 있다. = templates에서 {% url 'name' %} 이런 식으로 적은 경우
# 해당 name을 찾아서 갈 수 있다.
# /three/create 를
# url 'res-create' 이런 식으로 변경할 수 있다.