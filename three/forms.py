from django.forms import ModelForm
from django import forms
from three.models import Food
from three.models import Review

class FoodForm(ModelForm):
    class Meta:
        model=Food
        fields=['name','adr','pw']
        labels={
            'name':'이름',
            'adr':'주소',
            'pw':'비밀번호',
        }
        widgets={
            'pw':forms.PasswordInput()
        }

class UpdateFoodForm(FoodForm):
    class Meta:
        model=Food
        exclude=['pw']








Review_Score=(
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
    ('5',5),
)
class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields=['score','comment','res']
        labels={
            'score':'평점',
            'comment':'코멘트',
        }
        widgets={
            'res':forms.HiddenInput(),
            'score':forms.Select(choices=Review_Score,attrs={'class':'form-control'}),
            'comment':forms.Textarea(attrs={'class':'form-control','rows':3})
        }




