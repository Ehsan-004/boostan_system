from django.urls import path
from .views import SideMenuView, profile

app_name = 'request_manager'

urlpatterns = [
    path('sideMenu/', SideMenuView.as_view(), name='sidemenu'),
    path('profile/', profile, name='profile'),
]
