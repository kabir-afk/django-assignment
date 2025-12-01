from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bank, Branch
from .serializers import BankSerializer,BranchSerializer

# Create your views here.
class Banks(APIView):
    def get(self,req):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks ,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class Branches(APIView):
    def get(self, req):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)