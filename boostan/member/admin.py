from django.contrib import admin
from .models import Member, Teacher, Student, Course, Score


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'position')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('member_profile', 'personnel_code')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('member_profile', 'department')

class ScoreAdmin(admin.ModelAdmin):
    list_display = ('score', )

admin.site.register(Course, CourseAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Score, ScoreAdmin)