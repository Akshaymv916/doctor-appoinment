from django.conf import settings
from django.urls import path

from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('get_doctors',views.get_doctor,name='get_doctors'),
    path('appoinment',views.appoinment,name='appoinment'),
    path('clear',views.clear,name='clear'),
]
