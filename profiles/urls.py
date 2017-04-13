from django.conf.urls import url
from django.conf.urls import patterns

from . import views

urlpatterns = patterns('',
    url(
        r'^(?P<username>[\w.@+-]+)/$',
        views.profile,
        name='profile'
    ),

)