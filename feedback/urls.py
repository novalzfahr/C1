from django.urls import path
from .views import *

app_name = "feedback"

urlpatterns = [
    path('', read_feedback, name='read_feedback'),
    path('create/', create_feedback, name='create_feedback'),
    # path('create/', create_feedback.as_view(), name='create_feedback'),
]