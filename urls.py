#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
import school_app
from school_app import views
from school_app.views import StudentViewSet, ClassroomViewSet, \
    HomePageView

router = routers.SimpleRouter()

router.register(r'classrooms', ClassroomViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = router.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^classrooms/$',
        school_app.views.ClassroomViewSet.as_view({'get': 'list'}),
        name='classroom-list'),
    url(r'^classrooms/(?P<pk>[0-9]+)$',
        school_app.views.ClassroomViewSet.as_view({'get': 'list'}),
        name='classroom-list'),
    url(r'^students/$',
        school_app.views.StudentViewSet.as_view({'get': 'list'}),
        name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)$',
        school_app.views.StudentViewSet.as_view({'get': 'list'}),
        name='student-list'),
    url(r'^', HomePageView.as_view(), name='index-page'),
    url(r'^', include(router.urls)),
    ]

