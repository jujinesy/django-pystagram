# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from django170219.core import views as core_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django170219.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admi[a-z0-9]/', include(admin.site.urls)),


    url(r'^photo/(?P<pk>\d+)$', 'Photos.views.single_photo', name='view_single_photo'),
    url(r'^photo/upload/$', 'Photos.views.new_photo', name='new_photo'),

    url(
        r'^accounts/login/',
        auth_views.login,
        name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(
        r'^accounts/logout/',
        auth_views.logout,
        name='logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
        }
    ),

    url(r'^users/', include('profiles.urls')),


    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/password/$', core_views.password, name='password'),
)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )