# from django.shortcuts import render
from rest_framework import viewsets         
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer, JobSerializer, CandidateSerializer
from app_sgrt.models import Customer, Job, Candidate
from rest_framework import generics


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

@api_view(['GET'])
def customerList(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customerDetail(request, pk):
    customers = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customers, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def customerCreate(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def customerUpdate(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def customerDelete(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return Response('Customer was deleted!')

@api_view(['GET'])
def jobList(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def jobDetail(request, pk):
    jobs = Job.objects.get(id=pk)
    serializer = JobSerializer(jobs, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def jobCreate(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def jobUpdate(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(instance=job, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def jobDelete(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return Response('Job was deleted!')

@api_view(['GET'])
def candidateList(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data)  

@api_view(['GET'])
def candidateDetail(request, pk):
    candidates = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(candidates, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def candidateCreate(request):
    serializer = CandidateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def candidateUpdate(request, pk):
    candidate = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(instance=candidate, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def candidateDelete(request, pk):
    candidate = Candidate.objects.get(id=pk)
    candidate.delete()
    return Response('Candidate was deleted!')