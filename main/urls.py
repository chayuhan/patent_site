
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #환경설정
    path('admin/', admin.site.urls),
    
    #메인페이지 지정
    path('', views.index),
    path('index/', views.index),
    path('home/', views.index),



    #기능별 지정
    path('wait/', views.wait),             #로딩화면
    path('text_NER/', views.text_NER),       #요약문 개체명 조회
    
]