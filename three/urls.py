from django.urls import path
from . import views

urlpatterns=[
    path('li/',views.li,name='li'),
    path('create/', views.create, name='res-create'),
    path('update/', views.update, name='res-update'),
    path('food/<int:id>/', views.read, name='res-read'),
    #three/food/게시글 번호 맵핑
    path('delete/', views.delete, name='res-delete'),
    path('food/<int:food_id>/review/create/', views.review_create, name='review-create'),
    path('food/<int:food_id>/review/delete/<int:review_id>',
         views.review_delete,name='review-delete'),
    path('review/li/',views.review_li, name='review_li'),
    path('food/<int:id>/delete/',views.delete,name='res-delete')

]