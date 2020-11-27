from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('users/', views.UserViews.as_view()),
    path('users/<int:year>-<int:month>-<int:day>/', views.UserViews.as_view()),
]