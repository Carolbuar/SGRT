from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer, JobSerializer, CandidateSerializer
from app_sgrt.models import Customer, Job, Candidate

@api_view(['GET'])
def customers_list(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_customer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)