from django.urls import path
from .views import Banks , Branches

urlpatterns = [
    path('', Banks.as_view()),
    path('branches/<str:ifsc>', Branches.as_view()),
]