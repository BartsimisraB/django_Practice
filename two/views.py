from django.shortcuts import render
from two.models import Board
from .forms import BoardForm
from django.http import HttpResponseRedirect


def list(request):
    con = {'n': Board.objects.all()}
    return render(request, 'two/list.html', con)


def fo(request):
    # form = BoardForm()
    # return render(request, 'two/fo.html', {'form': form})
    if request.method == 'POST':    # fo 주소로 POST 방식으로 데이터가 전달됨
        form = BoardForm(request.POST)  # request의 POST 데이터를 바로 BoardForm에 담겠다.
        if form.is_valid():  # 입력 Form에서 Model에 설정한 유효성 검사를 만족한다면
            a = form.save() # save 함수를 이용해 입력받은 데이터가 유효하다면 저장
            # print(form)
        return HttpResponseRedirect('/list/')
    form = BoardForm()
    return render(request, 'two/fo.html', {'form': form})


def check(request):
    form = BoardForm(request.POST)  # def fo에서 넣은 값이 POST인 경우
    if form.is_valid():  # 입력데이터가 form클래스에서 정의한 조건에 만족하는지 체크한다
        return render(request, 'two/check.html', {'form': form})
    return HttpResponseRedirect('/fo/')  # 입력데이터가 유효하지 않으면 되돌아간다
