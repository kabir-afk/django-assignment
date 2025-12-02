from django.urls import path
from .views import BankListView,BankCitiesListView,BankStateListView,BankDetailView,BankBranchListView,BranchListView,BranchDetailView , BranchValidateView

urlpatterns = [
    path('banks', BankListView.as_view()),
    path('banks/<int:id>', BankDetailView.as_view()),
    path('banks/<int:id>/cities', BankCitiesListView.as_view()),
    path('banks/<int:id>/states', BankStateListView.as_view()),
    path('banks/<int:id>/branches', BankBranchListView.as_view()),
    path('branches', BranchListView.as_view()),
    path('branches/<str:ifsc>', BranchDetailView.as_view()),
    path('branches/<str:ifsc>/validate', BranchValidateView),
]