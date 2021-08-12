from django.urls import path, include

from school.views import index, fufel,spisok_edu,order

urlpatterns = [

    path('', index,name='home'),
    path('about/', fufel, name='about'),
    path('order/', order, name='order'),

]