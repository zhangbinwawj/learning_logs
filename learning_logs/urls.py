"""定义lerning_logs的URl模式"""

from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path(r'', views.index, name='index'),
    path(r'topics/', views.index, name='index'),
]