from django.shortcuts import get_object_or_404
from rest_framework import status , generics , filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bank, Branch
from .serializers import BankSerializer,BranchSerializer,CitySerializer , StateSerializer
from .utils import BranchFilter

# Create your views here.
class BankListView(APIView):
    def get(self,req):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class BankDetailView(APIView):
    def get(self,req,id):
        banks = get_object_or_404(Bank, id=id)
        serializer = BankSerializer(banks)
        return Response(serializer.data,status=status.HTTP_200_OK)
class BankBranchListView(generics.ListAPIView):
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['bank_name','branch_name','state', 'city', 'district']
    filterset_class = BranchFilter

    def get_queryset(self):
        bank_id = self.kwargs["id"]
        return Branch.objects.filter(bank=bank_id).order_by('pk')
class BankCitiesListView(generics.ListAPIView):
    serializer_class = CitySerializer

    def get_queryset(self):
        bank_id = self.kwargs["id"]
        return Branch.objects.filter(bank=bank_id).values('city').distinct().order_by('city')
class BankStateListView(generics.ListAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        bank_id = self.kwargs["id"]
        return Branch.objects.filter(bank=bank_id).values('state').distinct().order_by('state')
    
class BranchListView(generics.ListAPIView):
    queryset = Branch.objects.order_by('pk')
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['bank_name','branch_name','state', 'city', 'district']
    filterset_class = BranchFilter

class BranchDetailView(APIView):
    def get(self, req,ifsc):
        branch = get_object_or_404(Branch, ifsc=ifsc)
        serializer = BranchSerializer(branch)
        return Response(serializer.data, status=status.HTTP_200_OK)

def BranchValidateView(self, req,ifsc):
    try:
        Branch.objects.get(ifsc=ifsc)
        return Response("Valid IFSC",status=status.HTTP_200_OK)
    except Branch.DoesNotExist:
        return Response("Invalid IFSC",status=status.HTTP_404_NOT_FOUND)