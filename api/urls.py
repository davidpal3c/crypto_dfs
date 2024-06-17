from django.urls import path 
from . import views

app_name = 'api'

urlpatterns = [
    path('current_df/', views.current_df, name='current_df')
]