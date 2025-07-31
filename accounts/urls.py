from django.urls import path
from . import views #from accounts import views (this is also correct)

urlpatterns = [
    path('', views.login_view, name='root_login'),
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
