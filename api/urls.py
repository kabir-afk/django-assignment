from django.urls import path
from .views import Banks

urlpatterns = [
    path('', Banks.as_view()),
]