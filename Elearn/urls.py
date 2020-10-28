
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hp,name='hp'),
    path('home/', views.home,name='home'),
    path('courses/',views.list,name='courses'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('create_course/',views.create_course,name='create_course'),
    path('contents/<str:pk>/',views.contents,name='contents'),
    path('contact/',views.contact,name='contact'),

    path('contents/<str:pk>/',views.contents,name='contents'),

    path('enroll_course/',views.enroll_course,name='enroll_course'),
    path('contents/<str:pk>/',views.contents,name='contents'),
    
    path('update_enroll/<str:pk>/',views.update_enroll,name='update_enroll'),
    path('remove_student/<str:pk>/',views.remove_enroll,name='remove_student'),
    path('remove_enroll/<str:pk>/',views.remove_uenroll,name='remove_enroll'),

]
