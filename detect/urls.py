from django.urls import path
from detect import views

urlpatterns=[
    path('main/',views.main, name='main'),
    path('main/detect/',views.detect, name='detect'),
    path('main/login/',views.login, name='login'),
    path('main/contact/',views.contact, name='contact'),
    path('main/about/',views.about, name='about'),
    path('main/service/',views.service, name='service'),
    # url(r'^main/$', 'views.main',name='main'),
    # url(r'^detect/$', 'views.detect',name='detect'),
    # url(r'^contact/$', 'views.contact',name='contact'),

]