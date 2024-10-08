
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, email_verification, UserPasswordResetView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('confirm/<str:token>/', email_verification, name='confirm'),
    path("password-reset/", UserPasswordResetView.as_view(), name="password_reset"),
]