from django.urls import path
from socialweb import views


urlpatterns= [
    path("signup",views.SignUpView.as_view(),name="register"),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.HomeView.as_view(),name="home"),
    path("userprofile",views.ProfileCreateView.as_view(),name="userprofile"),
    path("profile",views.UserprofileView.as_view(),name="profile_detail")

]