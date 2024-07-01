from django.contrib import admin
from .models import Member, Teacher, Student, Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'position')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('member_profile', 'personnel_code')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('member_profile', 'department')

admin.site.register(Course, CourseAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)