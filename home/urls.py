from django.conf.urls import url
from home.views import HomeView
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(HomeView.as_view()), name='home'), ## I use the login_required decorators in the urls because i find it hard on the views
    url(r'^connect/(?P<operation>.+)(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]
