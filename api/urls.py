from django.urls import path
from .views import Banks , All_bank_branches ,Branch_by_IFSC_code

urlpatterns = [
    path('', Banks.as_view()),
    path('branches', All_bank_branches.as_view()),
    path('branches/<str:ifsc>', Branch_by_IFSC_code.as_view()),
]