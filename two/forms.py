from django import forms
from django.forms import ModelForm
from two.models import Board


# 부모가 forms.Form
# django의 forms를 상속받는 클래스 BoardForm

# class BoardForm(forms.Form):
#     title = forms.CharField(label='타이틀', max_length=50)
#     content = forms.CharField(label='컨텐츠', widget=forms.Textarea)

# ModelForm 사용시
class BoardForm(ModelForm):
    # Meta 클래스를 필수로 작성해야 한다.
    # Meta 클래스는 아래와 같이 작성한다.
    class Meta:
        # 모델 폼이 사용할 모델과
        model = Board
        # 모델의 필드들 작성
        fields = ['title', 'content']
        #
        labels = {
            'title': '타이틀',
            'content': '콘텐츠',
        }
        error_messages = {
            'name': {
                'max_length': '20자 이하로 주세요'
            }
        }
