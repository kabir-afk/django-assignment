from rest_framework import status , generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Bank, Branch
from .serializers import BankSerializer,BranchSerializer

# Create your views here.
class Banks(APIView):
    def get(self,req):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class All_bank_branches(generics.ListAPIView):
    pagination_class = PageNumberPagination
    queryset = Branch.objects.order_by('pk')
    serializer_class = BranchSerializer
    
class Branch_by_IFSC_code(APIView):
    def get(self, req,ifsc):
        branches = Branch.objects.get(ifsc=ifsc)
        serializer = BranchSerializer(branches)
        return Response(serializer.data, status=status.HTTP_200_OK)