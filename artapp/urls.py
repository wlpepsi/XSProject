from django.conf.urls import url
from .views import index

urlpatterns = [
    # 主页面url
    url(r'^index/',index,name='index' ),
]