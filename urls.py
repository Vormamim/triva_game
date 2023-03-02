from django.urls import path
from trivia.views import trivia

urlpatterns = [
    path('trivia/', trivia, name='trivia'),
]
