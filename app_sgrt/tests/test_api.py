from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Customer, Job, Candidate
from api.serializers import CustomerSerializer, JobSerializer, CandidateSerializer

class CustomerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer1 = Customer.objects.create(
            name='Customer 1', 
            email='customer1@example.com', 
            address='123 Main St', 
            phone='555-1234', 
            representative_name='John Doe'
        )
    
        
    def test_create_customer(self):
        url = reverse('customer_create')
        data = {'name': 'New Customer', 
                'email': 'newcustomer@example.com', 
                'address': '456 Elm St', 
                'phone': '555-5678', 
                'representative_name': 'Jane Doe'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2) 

    def test_list_customers(self):
        url = reverse('customer_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_customer(self):
        url = reverse('customer_detail', args=[self.customer1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.customer1.name)

    def test_update_customer(self):
        url = reverse('customer_update', args=[self.customer1.id])
        data = {'name': 'Updated Customer Name',
                'email': 'customer1@example.com', 
                'address': '456 Elm St', 'phone': '555-5678', 
                'representative_name': 'Jane Doe'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer1.refresh_from_db()
        self.assertEqual(self.customer1.name, 'Updated Customer Name')

    def test_delete_customer(self):
        url = reverse('customer_delete', args=[self.customer1.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(id=self.customer1.id).exists())

class JobAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='testcustomer@example.com',
            website='http://example.com',
            address='123 Test St',
            phone='1234567890',
            representative_name='John Doe'
        )
        self.job = Job.objects.create(
            name='Test Job',
            status='open',
            customer=self.customer,
            description='Test job description',
            location='Test location'
        )

    def test_create_job(self):
        url = reverse('job_create')
        initial_job_count = Job.objects.count()
        job_data = {
            'name': 'Test Job',
            'status': 'open',
            'customer': self.customer,
            'description': 'Test job description',
            'location': 'Test location'
        }
        response = self.client.post(url, job_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), initial_job_count + 1)
        self.assertEqual(Job.objects.last().name, 'Test Job')

    def test_list_jobs(self):
        url = reverse('job_list')
        job1 = Job.objects.create(
            name='Test Job 1',
            status='open',
            customer=self.customer,
            description='Test job 1 description',
            location='Test location 1'
        )

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_job(self):
        url = reverse('job_detail', args=[self.job.id])
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Job')

    def test_update_job(self):
        url = reverse('job_update', args=[self.job.id])
        
        job_data = {
            'name': 'Updated Job',
            'status': 'closed',
            'customer': self.customer,
            'description': 'Updated job description',
            'location': 'Updated location'
        }
        response = self.client.put(url, job_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Job.objects.get(id=self.job.id).name, 'Updated Job')

    def test_delete_job(self):
        url = reverse('job_delete', args=[self.job.id])
        initial_job_count = Job.objects.count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Job.objects.count(), initial_job_count - 1)

class CandidateAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(
            name='Test Customer',
            email='testcustomer@example.com',
            website='http://example.com',
            address='123 Test St',
            phone='1234567890',
            representative_name='John Doe'
        )
        self.job = Job.objects.create(
           name='Test Job',
           status='open',
           customer=self.customer,
           description='Test job description',
           location='Test location'
        )
        self.candidate = Candidate.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane.doe@example.com',
            skills='Java, C++, SQL',
        )

    def test_create_candidate(self):
        url = reverse('candidate_create')
        initial_candidate_count = Candidate.objects.count()
        candidate_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'skills': 'Python, Django, JavaScript'
        }
        response = self.client.post(url, candidate_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), initial_candidate_count + 1)
        self.assertEqual(Candidate.objects.last().first_name, 'John')

    def test_list_candidates(self):
        url = reverse('candidate_list')
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_candidate(self):
        url = reverse('candidate_detail', args=[self.candidate.id])
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')

    def test_update_candidate(self):
        url = reverse('candidate_update', args=[self.candidate.id])
        
        candidate_data = {
            'first_name': 'Updated Jane',
            'last_name': 'Updated Doe',
            'email': 'updated.jane.doe@example.com',
            'skills': 'Python, Django, JavaScript',
        }
        response = self.client.put(url, candidate_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Candidate.objects.get(id=self.candidate.id).first_name, 'Updated Jane')

    def test_delete_candidate(self):
        url = reverse('candidate_delete', args=[self.candidate.id])
        
        initial_candidate_count = Candidate.objects.count()
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Candidate.objects.count(), initial_candidate_count - 1)