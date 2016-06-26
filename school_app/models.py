from django.db import connection, models
from django.contrib.auth.models import User


class School(models.Model):
	school_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	
	def __str__(self):
		return self.school_name
	
class Classroom(models.Model):
	school = models.ForeignKey(School, related_name='schools')
	academic_year = models.CharField(max_length=9)
	classroom = models.CharField(max_length=100)
	floor = models.IntegerField(default=0)
	
	class Meta:
		unique_together = (('school', 'classroom', 'academic_year'),)
	
	def __str__(self):
		return self.classroom

class Student(models.Model):
	classroom = models.ForeignKey(Classroom, related_name='students')
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=60)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	birthday = models.DateField()
	
	def _get_full_name(self):
		return u'%s %s' % (self.first_name, self.last_name)
	
	def __str__(self):
		return u"{0} {1}, {2}".format(self.first_name, self.last_name, self.classroom.school)

