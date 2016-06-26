#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from models import School, Classroom, Student
from django import forms


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'city', 'address')


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'school', 'academic_year', 'floor')


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'classroom', 'gender',
                  'birthday')


class StudentAdmin(admin.ModelAdmin):

    def get_school(self, obj):
        return obj.classroom.school

    get_school.short_description = 'School'
    get_school.admin_order_field = 'classroom__school'

    list_display = ('first_name', 'last_name', 'gender', 'classroom',
                    'get_school')
    raw_id_fields = ('classroom', )
    form = StudentForm
    search_fields = ['first_name', 'last_name']


admin.site.register(School, SchoolAdmin)
admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Student, StudentAdmin)

