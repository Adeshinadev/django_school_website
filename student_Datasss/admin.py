from django.contrib import admin
from .models import Student_data,Term,Class_of_student,Year,Subject_name,Student_Result,Result_extra

# Register your models here.
admin.site.register(Term)
admin.site.register(Class_of_student)
admin.site.register(Year)
admin.site.register(Result_extra)
admin.site.register(Student_data)
admin.site.register(Subject_name)
admin.site.register(Student_Result)
