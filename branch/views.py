from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer

class BankListView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BranchDetailView(APIView):
    def get(self, request, ifsc):
        try:
            branch = Branch.objects.get(ifsc=ifsc)
            serializer = BranchSerializer(branch)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Branch.DoesNotExist:
            return Response({"error": "Branch not found"}, status=status.HTTP_404_NOT_FOUND)