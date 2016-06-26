#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import TemplateView
from django.template import RequestContext
from rest_framework import viewsets
from rest_framework.decorators import api_view
from school_app.models import School, Classroom, Student
from school_app.serializers import StudentSerializer, \
    ClassroomSerializer


class HomePageView(TemplateView):
    template_name = 'school_app/base.html'


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    
