from django.urls import path
from .views import SideMenuView, profile, admin_all

app_name = 'request_manager'

urlpatterns = [
    path('sideMenu/', SideMenuView.as_view(), name='sidemenu'),
    path('profile/', profile, name='profile'),
    path('admin_all/', admin_all, name='admin_all'),
]
