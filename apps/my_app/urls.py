from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$',views.courses),
    url(r'^destroy/(?P<id>\d+)', views.confirm),
    url(r'^confirm/(?P<id>\d+)', views.destroy)

]

## not sure why when you go to the confirm page it routes back to destroy

