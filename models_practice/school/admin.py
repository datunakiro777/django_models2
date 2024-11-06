from django.contrib import admin
from school.models import Classroom, Student, Teacher

admin.site.register(Classroom)
admin.site.register(Teacher)
admin.site.register(Student)
