from django.shortcuts import render
from three.models import Food  # models 가 DB를 의미
from django.core.paginator import Paginator


def li(reqeust):
    res = Food.objects.all()
    paginator = Paginator(res, 5)   # 한 페이지당 5개
    page = reqeust.GET.get('page')
    a = paginator.get_page(page)

    con = {'res': a}
    return render(reqeust, 'three/li.html', con)


def basic(request):
    con = {'res': Food.objects.all()}
    return render(request, 'three/basic.html', con)
