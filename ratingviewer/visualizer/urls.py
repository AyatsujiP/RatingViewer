from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('ranking/$', views.ranking, name='index'),
    url('user/search/$',views.user_search,name='user_search'),
    url('user/search_result/$',views.user_search_result,name='user_search'),    
    path('user/<str:ncs_id>/',views.user_index,name='user_index'),    
]