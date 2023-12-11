from django.urls import path
from .views import *

app_name = "feedback"

urlpatterns = [
    path('', read_feedback, name='read_feedback'),
    path('create/', create_feedback, name='create_feedback'),
    path('delete/<int:feedback_id>/', delete_feedback, name='delete_feedback'),
]