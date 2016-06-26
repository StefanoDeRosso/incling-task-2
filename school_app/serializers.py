#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from school_app.models import School, Classroom, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('classroom', 'first_name', 'last_name', 'gender',
                  'birthday')


class ClassroomSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Classroom
        depth = 1
        fields = ('school', 'academic_year', 'classroom', 'floor',
                  'students')

