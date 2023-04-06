from django.forms import ModelForm
from django import forms
from three.models import Food, Review


# 폼 형식 지정 파일

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'adr', 'pw']
        labels = {
            'name': '음식 이름',
            'adr': '음식점 주소',
            'pw': '비밀번호',
        }
        # widgets에서 attrs를 이용해 클래스를 지정할 수 있다.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'adr': forms.TextInput(attrs={'class': 'form-control'}),
            'pw': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


Review_Score = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['score', 'comment', 'res']
        labels = {
            'score': '평점',
            'comment': '댓글',
        }
        # widgets :
        widgets = {
            'res': forms.HiddenInput(),  # review 를 작성할 식당 정보는 사용자에게 보이지 않겠다.
            # 평점(Review_Score)을 select로 구성하겠다
            'score': forms.Select(choices=Review_Score, attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
