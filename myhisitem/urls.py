"""定义myhisitem的URl模式"""

from django.urls import path

from . import views

urlpatterns = [
    # 主页
    path(r'his/', views.index, name='index')
]