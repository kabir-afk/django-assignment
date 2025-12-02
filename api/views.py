from rest_framework import status , generics , filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bank, Branch
from .serializers import BankSerializer,BranchSerializer
from .utils import BranchFilter

# Create your views here.
class BankListView(APIView):
    def get(self,req):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class BankDetailView(APIView):
    def get(self,req,id):
        banks = Bank.objects.get(id=id)
        serializer = BankSerializer(banks)
        return Response(serializer.data,status=status.HTTP_200_OK)
class BankBranchListView(generics.ListAPIView):
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['bank_name__name','branch_name','state', 'city', 'district']
    filterset_class = BranchFilter

    def get_queryset(self):
        bank_id = self.kwargs["id"]
        return Branch.objects.filter(bank_name=bank_id).order_by('pk')
    
class BranchListView(generics.ListAPIView):
    queryset = Branch.objects.order_by('pk')
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['bank_name__name','branch_name','state', 'city', 'district']
    filterset_class = BranchFilter

class BranchDetailView(APIView):
    def get(self, req,ifsc):
        branches = Branch.objects.get(ifsc=ifsc)
        serializer = BranchSerializer(branches)
        return Response(serializer.data, status=status.HTTP_200_OK)