from django.conf.urls.static import static
from django.urls import path
from .views import StudentLoginView, RegisterView, LogoutView
from boostan.settings import MEDIA_ROOT, MEDIA_URL

app_name = 'members'

urlpatterns = [
    path('login/', StudentLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
