from django.urls import path, include
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.intro, name='intro'),
    path('intro/', views.intro, name='intro'),
    path('wk01/', views.wk01, name='wk01'),
    path('wk02/', views.wk02, name='wk02'),
    path('wk03/', views.wk03, name='wk03'),
    path('performance/', views.performance, name='performance'),
    path('save_summary/', views.save_weekly_summary, name='save_summary'),
]

