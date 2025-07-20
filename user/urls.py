from django.urls import path

from user import views

app_name = "user"

urlpatterns = [
    path("login",views.login_view,name="login"),
    path("registration",views.registration_view,name="registration"),
    path("logout",views.user_logout,name="logout"),
    path("verify/<uidb64>/<token>/",views.verify_email,name="verify_email"),
    path("profile",views.profile,name="profile"),
]
