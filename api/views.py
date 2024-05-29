# from django.shortcuts import render
from rest_framework import viewsets, status   
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from .serializers import CustomerSerializer, JobSerializer, CandidateSerializer
from app_sgrt.models import Customer, Job, Candidate
import django_filters
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import JobFilter



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobFilter

@api_view(['GET'])
def customerList(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customerDetail(request, pk):
    try:
        customers = Customer.objects.get(id=pk)
        serializer = CustomerSerializer(customers, many=False)
        return Response(serializer.data)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def customerCreate(request):
    serializer = CustomerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def customerUpdate(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(instance=customer, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def customerDelete(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        customer.delete()
        return Response('Customer was deleted!', status=status.HTTP_204_NO_CONTENT)

    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def jobList(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def jobDetail(request, pk):
    try:
        jobs = Job.objects.get(id=pk)
        serializer = JobSerializer(jobs, many=False)
        return Response(serializer.data)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def jobCreate(request):
    serializer = JobSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def jobUpdate(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(instance=job, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def jobDelete(request, pk):
    try:
        job = Job.objects.get(id=pk)
        job.delete()
        return Response('Job was deleted!', status=status.HTTP_204_NO_CONTENT)

    except Job.DoesNotExist:
        return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def candidateList(request):
    candidates = Candidate.objects.all()
    serializer = CandidateSerializer(candidates, many=True)
    return Response(serializer.data)  

@api_view(['GET'])
def candidateDetail(request, pk):
    try:
        candidates = Candidate.objects.get(id=pk)
        serializer = CandidateSerializer(candidates, many=False)
        return Response(serializer.data)
    except Candidate.DoesNotExist:
        return Response({'error': 'Candidate not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def candidateCreate(request):
    serializer = CandidateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def candidateUpdate(request, pk):
    candidate = Candidate.objects.get(id=pk)
    serializer = CandidateSerializer(instance=candidate, data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Candidate.DoesNotExist:
        return Response({'error': 'Candidate not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def candidateDelete(request, pk):
    try:
        candidate = Candidate.objects.get(id=pk)
        candidate.delete()
        return Response('Candidate was deleted!', status=status.HTTP_204_NO_CONTENT)

    except Candidate.DoesNotExist:
        return Response({'error': 'Candidate not found.'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def addCandidateToJob(request, candidate_id, job_id):
    try:
        candidate = Candidate.objects.get(id=candidate_id)
        job = Job.objects.get(id=job_id)
    except Candidate.DoesNotExist:
        return Response({'error': 'Candidate not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)

    candidate.applied_jobs.add(job)
    candidate.save()

@api_view(['GET'])
def candidatesAppliedToJob(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        candidates = job.candidates.all()
        serializer = CandidateSerializer(candidates, many=True)
        return Response(serializer.data)
    except Job.DoesNotExist:
        return Response({'error': 'Job not found.'}, status=status.HTTP_404_NOT_FOUND)