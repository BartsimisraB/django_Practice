from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader  # template 파일 연결을 위한 import 모듈
from datetime import datetime
import random

# loader를 이용해 render 사용하기
def index(request):
    now_T = datetime.now()
    # templates 디렉토리 안의 index.html 파일 load
    tem = loader.get_template('index.html')
    # context에 들어가는 딕셔너리를
    context = {'now_time': now_T}
    # return 시 담아서 띄우겠다.
    return HttpResponse(tem.render(context, request))


# Create your views here.
# loader를 이용하지 않고 render 하는 방법
def number(request):
    con = {'num': 3}
    # 숏 코딩 : 인자값만 넘겨서 간략하게 코딩 가능
    return render(request, 'first/number.html', con)


# form에서 GET방식으로 input의 name을 이용해
# 파라미터로 받아온다
def result(request):
    a=int(request.GET['num'])  #15

    re=list() #[15]

    if a>=1 and a<=40:
        re.append(a)

    re2=list() #[]
    for i in range(0,40):
        if a!=i+1:
            re2.append(i+1)

    random.shuffle(re2)

    while len(re) < 10:
        re.append(re2.pop())

    con={'id':re}

    return render(request,'first/result.html',con)
