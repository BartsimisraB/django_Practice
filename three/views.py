from django.shortcuts import render, get_object_or_404, redirect  # get_object_or_404 로 에러 페이지 변경
from three.models import Food, Review  # models 가 DB를 의미
from django.core.paginator import Paginator
from three.forms import FoodForm, ReviewForm
from django.http import HttpResponseRedirect


def li(reqeust):
    res = Food.objects.all()
    paginator = Paginator(res, 5)  # 한 페이지당 5개
    page = reqeust.GET.get('page')
    a = paginator.get_page(page)

    con = {'res': a}
    return render(reqeust, 'three/li.html', con)


def create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            a = form.save()
        return HttpResponseRedirect('/three/li/')
    form = FoodForm()
    return render(request, 'three/create.html', {'form': form})


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        # a = Food.objects.get(pk=request.POST.get('id'))
        a = get_object_or_404(Food, pk=request.POST.get('id'))  # 에러 발생시 404 페이지가 나오게 만듬
        pw = request.POST.get('pw', "")
        form = FoodForm(request.POST, instance=a)  # 수정할 대상 객체 지정

        if form.is_valid() and pw == a.pw:
            a = form.save()  # 수정한 데이터를 테이블에 저장

    elif 'id' in request.GET:  # 데이터를 가져올 때는 GET 방식
        # a = Food.objects.get(pk=request.GET.get('id'))
        a = get_object_or_404(Food, pk=request.GET.get('id'))
        form = FoodForm(instance=a)  # 수정된 데이터 저장
        return render(request, 'three/update.html', {'form': form})  # 가져온 데이터를 해당 url로 넘김

    return HttpResponseRedirect('/three/li')

    # def read(request):
    #     if 'id' in request.GET:  # id 값이 존재하는지 확인
    #         a = get_object_or_404(Food, pk=request.GET.get('id'))
    #         return render(request, 'three/read.html', {'a': a})
    #     return HttpResponseRedirect("/three/li")


# id (pk) 를 url 파라미터를 통해 전달받는다.
def read(request, id):  # urls.py 에서 작성한 <int:id>로 받은 파라미터를 사용하는 방식

    if id is not None:  # id 값이 존재하는지 확인
        a = get_object_or_404(Food, pk=id)
        re = Review.objects.filter(res=a).all()    # 음식에 대한 리뷰를 전부 들고와서 re로 담아 보낸다
        return render(request, 'three/read.html', {'a': a, 're': re})
    return HttpResponseRedirect("/three/li")

#


def delete(request):
    if 'id' in request.GET:
        a = get_object_or_404(Food, pk=request.GET.get('id'))
        a.delete()
    return HttpResponseRedirect('/three/li')


def review_create(request, food_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            a = form.save()
        # HttpResponseRedirect와 같은 의미
        # redirect는 view name을 기반으로 움직인다. (조금 더 간편함)
        # url이 변경되도 view name 이 그대로면 변경하지 않아도 된다.
        return redirect('res-read', id=food_id)

    a = get_object_or_404(Food, pk=food_id)
    form = ReviewForm(initial={'res': a})
    return render(request, 'three/review_create.html', {'form': form, 'a': a})


def review_delete(request, food_id, review_id):
    a = get_object_or_404(Review, pk=review_id)
    a.delete()
    return redirect('res-read', id=food_id)
