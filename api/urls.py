from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    # 网页端接口
    path('login/', views.AuthView.as_view()),

]