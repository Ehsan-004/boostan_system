from django.urls import path
from .views import SideMenuView, profile, admin_all, member_courses, student_scores

app_name = 'request_manager'

urlpatterns = [
    path('sideMenu/', SideMenuView.as_view(), name='sidemenu'),
    path('profile/', profile, name='profile'),
    path('admin_all/', admin_all, name='admin_all'),
    path('courses/', member_courses, name='member_courses'),
    path('scores/', student_scores, name='student_scores'),
]
