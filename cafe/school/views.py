from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
menu=['Про сайт','Заказати страву','Корзина', 'Увійти']
def index(request):

    return render(request,'school/index.html',{'title':'Меню їдальні','menu':menu})
def spisok_edu(request,nomer):
    if int(nomer)>5:

        return redirect('home',permanent=False)
    else:
        return HttpResponse(f'Ви вибрали {nomer}')

def fufel(request):

        return render(request, 'school/about.html',{'author':'Maslovskii'})


def order(request):
    return render(request, 'school/cart.html', {'cart': 'Корзина пуста'})