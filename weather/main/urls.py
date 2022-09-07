from django.urls import path, include
from main import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='register'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('emails/', views.EmailsView.as_view(), name='emails'),
]