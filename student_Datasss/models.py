from django.db import models
from account.models import User
from secschoolportal import settings

# Create your models here.

from django.db import models

# Create your models here.
class Student_data(models.Model):
    full_name=models.CharField(max_length=255)
    year_of_admission=models.CharField(max_length=23)
    D_O_B=models.CharField(max_length=100)
    Age=models.CharField(max_length=5)
    gender = models.CharField(max_length=255)
    local_government_area = models.CharField(max_length=255)
    state_of_origin = models.CharField(max_length=255)
    Religion = models.CharField(max_length=255)
    admission_number=models.CharField(max_length=4, default='1506')
    registered_username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.admission_number



class Subject_name(models.Model):
    Subject_name=models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.Subject_name

class Class_of_student(models.Model):
    class_of_student=models.CharField(max_length=30,primary_key=True,default='this')
    # year implies 2019/2020 or so
    # class_type implies A or B or C, that's JSS1A or JSS1B

    def __str__(self):
        return self.class_of_student



class Year(models.Model):
    year=models.CharField(max_length=20,primary_key=True,default='is')
    # year implies 2019/2020 or so
    # class_type implies A or B or C, that's JSS1A or JSS1B
    def __str__(self):
        return self.year

class Term(models.Model):
    term = models.CharField(max_length=255,primary_key=True,default='emptyoo')

    def __str__(self):
        return self.term


class Student_Result(models.Model):
    users=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    studentclass=models.ForeignKey(Class_of_student,on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    term=models.ForeignKey(Term,on_delete=models.CASCADE)
    subject_name=models.ForeignKey(Subject_name,on_delete=models.CASCADE)
    first_test=models.IntegerField()
    second_test=models.IntegerField()
    exam_score=models.IntegerField()
    score=models.IntegerField(null=True,blank=True)
    grade=models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.users)

class Result_extra(models.Model):
    studentclass = models.ForeignKey(Class_of_student, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    school_fee=models.CharField(max_length=20)
    next_term_resumption=models.DateField()
    studentclass_term_year=models.CharField(max_length=255)


    def __str__(self):
        return self.studentclass_term_year









