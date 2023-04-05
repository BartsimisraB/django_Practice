from django.forms import ModelForm
from three.models import Food

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'adr']
        labels = {
            'name': '음식 이름',
            'adr': '음식점 주소',
        }
