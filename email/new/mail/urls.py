from django.urls import path
from .import views
urlpatterns=[
    path("",views.mail,name='index'),
    path("session",views.session,name='session'),
    path("get",views.getsession,name='get')
]