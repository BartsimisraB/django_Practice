from django.shortcuts import render, get_object_or_404, redirect
from three.models import Food, Review
from django.core.paginator import Paginator
from three.forms import FoodForm, ReviewForm, UpdateFoodForm
from django.http import HttpResponseRedirect
from django.db.models import Count,Avg

def li(request):
    res=Food.objects.all().annotate(reviews_count=Count('review')).annotate(average_score=Avg('review__score'))
    paginator=Paginator(res,5) #한 페이지당 5개씩 표시
    page=request.GET.get('page')
    a=paginator.get_page(page)

    con={'res':a}
    return render(request, 'three/li.html', con)

#p.113
def create(request):
    if request.method=='POST':
        form=FoodForm(request.POST)
        if form.is_valid():
            a=form.save()
        return HttpResponseRedirect('/three/li/')
    form=FoodForm()
    return render(request,'three/create.html',{'form':form})

def update(request):
    if request.method=='POST' and 'id' in request.POST:
        a=get_object_or_404(Food, pk=request.POST.get('id'))
        pw=request.POST.get('pw',"")
        form=UpdateFoodForm(request.POST, instance=a)
        if form.is_valid() and pw==a.pw:
            a=form.save()
    elif 'id' in request.GET:
        a=get_object_or_404(Food, pk=request.GET.get('id'))
        form=FoodForm(instance=a)
        form.pw=''
        return render(request,'three/update.html',{'form':form})
    return HttpResponseRedirect('/three/li/')

#id(pk)를 url 파라미터를 통해 전달받는다
def read(request,id):
    if id is not None:
        a=get_object_or_404(Food, pk=id)
        re=Review.objects.filter(res=a).all()
        return render(request, 'three/read.html', {'a':a, 're': re})
    return HttpResponseRedirect('/three/li')

def delete(request,id):
    a = get_object_or_404(Food, pk=id)
    if request.method =='POST' and 'pw' in request.POST:
        if a.pw==request.POST.get('pw'):
            a.delete()
            return redirect('li')
        return redirect('res-read',id=id)
    return render(request,'three/delete.html',{'a':a})




def review_create(request,food_id):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            a=form.save()
        return redirect('res-read',id=food_id)
        #view name으로 움직이기 때문에 url이 변경되도 view name이 그대로면 변경하지않아도됨

    a=get_object_or_404(Food,pk=food_id)
    form=ReviewForm(initial={'res':a})
    return render(request, 'three/review_create.html',{'form':form, 'a':a})

def review_delete(request,food_id,review_id):
    a=get_object_or_404(Review,pk=review_id)
    a.delete()
    return redirect('res-read',id=food_id)

def review_li(request):
    reviews=Review.objects.all().select_related()
    paginator=Paginator(reviews, 10)

    page=request.GET.get('page')
    a=paginator.get_page(page)

    con={'reviews':a}
    return render(request,'three/review_li.html',con)


