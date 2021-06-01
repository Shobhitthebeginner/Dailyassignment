from django.urls import path
from .import views
from django.contrib.auth.views import
urlpatterns=[
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardViews,name="dashboard"),
    path('login/',views.loginViews,name="login"),
    path('register/',views.registerViews,name="register"),
    path('logout/',views.logoutViews,name="logout"),
]