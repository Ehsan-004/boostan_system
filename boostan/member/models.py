from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


def score_validator(score):
    if int(score) < 0 or int(score) > 20:
        raise ValidationError('نمره باید بین 0 تا 20 باشد.')
    return score


class Member(models.Model):
    positions = (
        ('student', 'student'),
        ('employee', 'employee'),
        ('teacher', 'teacher'),
        ('personnel', 'personnel'),
        ('admin', 'admin')
    )

    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10, unique=True)
    profile_picture = models.ImageField(upload_to='member_pictures', default='member_pictures/default.jpeg')
    position = models.CharField(max_length=10, choices=positions, default='personnel')

    class Meta:
        db_table = 'members'
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return self.user_profile.username + " " + self.position


class Student(models.Model):
    member_profile = models.OneToOneField(Member, on_delete=models.CASCADE)
    department = models.CharField(max_length=10)
    passed_terms = models.IntegerField(default=0)

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return  str(self.member_profile.user_profile)


class Teacher(models.Model):
    member_profile = models.OneToOneField(Member, on_delete=models.CASCADE)
    department = models.CharField(max_length=10)
    course_numbers = models.IntegerField(default=0)
    personnel_code = models.CharField(max_length=10)

    class Meta:
        db_table = 'teachers'
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return str(self.member_profile.user_profile.first_name) + " " + str(self.member_profile.user_profile.last_name)


class Personnel(models.Model):
    member_profile = models.OneToOneField(Member, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)

    class Meta:
        db_table = 'personnel'
        verbose_name = 'Personnel'
        verbose_name_plural = 'Personnel'

    def __str__(self):
        return "personnel-" + str(self.member_profile.national_code)


class Course(models.Model):
    name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'courses'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    score = models.IntegerField(default=0, validators=[score_validator,])

    class Meta:
        db_table = 'scores'
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
