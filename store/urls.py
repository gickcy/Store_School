
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/',views.register, name='register'),
    path('new_page/', views.new_page, name='new_page'),
    path('logout/', views.user_logout, name='logout'),
    path('student_form/', views.student_form, name='order_form')

]
