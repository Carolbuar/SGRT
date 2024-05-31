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
        data = {'name': 'New Customer', 'email': 'newcustomer@example.com', 'address': '456 Elm St', 'phone': '555-5678', 'representative_name': 'Jane Doe'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2) 

    def test_list_customers(self):
        url = reverse('customer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_customer(self):
        url = reverse('customer_detail', args=[self.customer1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.customer1.name)

    def test_update_customer(self):
        url = reverse('customer_update', args=[self.customer1.id])
        data = {'name': 'Updated Customer Name','email': 'newcustomer@example.com', 'address': '456 Elm St', 'phone': '555-5678', 'representative_name': 'Jane Doe'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer1.refresh_from_db()
        self.assertEqual(self.customer1.name, 'Updated Customer Name')

    def test_delete_customer(self):
        url = reverse('customer_delete', args=[self.customer1.id])
        response = self.client.delete(url)
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

    def test_create_job(self):
        initial_job_count = Job.objects.count()
        job_data = {
            'name': 'Test Job',
            'status': 'open',
            'customer': self.customer.id,
            'description': 'Test job description',
            'location': 'Test location'
        }
        response = self.client.post('/job-list/', job_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Job.objects.count(), initial_job_count + 1)
        self.assertEqual(Job.objects.last().name, 'Test Job')

    def test_list_jobs(self):
        Job.objects.create(
            name='Test Job 1',
            status='open',
            customer=self.customer,
            description='Test job 1 description',
            location='Test location 1'
        )
        Job.objects.create(
            name='Test Job 2',
            status='open',
            customer=self.customer,
            description='Test job 2 description',
            location='Test location 2'
        )
        response = self.client.get('/job-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_job(self):
        job = Job.objects.create(
            name='Test Job',
            status='open',
            customer=self.customer,
            description='Test job description',
            location='Test location'
        )
        response = self.client.get(f'/job-detail/{job.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Job')

    def test_update_job(self):
        job = Job.objects.create(
            name='Test Job',
            status='open',
            customer=self.customer,
            description='Test job description',
            location='Test location'
        )
        job_data = {
            'name': 'Updated Job',
            'status': 'closed',
            'customer': self.customer.id,
            'description': 'Updated job description',
            'location': 'Updated location'
        }
        response = self.client.put(f'/job-update/{job.id}/', job_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Job.objects.get(id=job.id).name, 'Updated Job')

    def test_delete_job(self):
        job = Job.objects.create(
            name='Test Job',
            status='open',
            customer=self.customer,
            description='Test job description',
            location='Test location'
        )
        initial_job_count = Job.objects.count()
        response = self.client.delete(f'/job-delete/{job.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Job.objects.count(), initial_job_count - 1)

class CandidateAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.job = Job.objects.create(
           name='Test Job',
           status='open',
           customer=1,
           description='Test job description',
           location='Test location'
           
        )

    def test_create_candidate(self):
        initial_candidate_count = Candidate.objects.count()
        candidate_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'resume': None,
            'skills': 'Python, Django, JavaScript',
            'applied_jobs': [self.job.id]
        }
        response = self.client.post('/candidate-list/', candidate_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), initial_candidate_count + 1)
        self.assertEqual(Candidate.objects.last().first_name, 'John')

    def test_list_candidates(self):
        Candidate.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane.doe@example.com',
            skills='Java, C++, SQL',
        )
        response = self.client.get('/candidate-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_candidate(self):
        candidate = Candidate.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane.doe@example.com',
            skills='Java, C++, SQL',
        )
        response = self.client.get(f'/candidate-detail/{candidate.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')

    def test_update_candidate(self):
        candidate = Candidate.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane.doe@example.com',
            skills='Java, C++, SQL',
        )
        candidate_data = {
            'first_name': 'Updated Jane',
            'last_name': 'Updated Doe',
            'email': 'updated.jane.doe@example.com',
            'skills': 'Python, Django, JavaScript',
        }
        response = self.client.put(f'/candidate-update/{candidate.id}/', candidate_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Candidate.objects.get(id=candidate.id).first_name, 'Updated Jane')

    def test_delete_candidate(self):
        candidate = Candidate.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane.doe@example.com',
            skills='Java, C++, SQL',
        )
        initial_candidate_count = Candidate.objects.count()
        response = self.client.delete(f'/candidate-delete/{candidate.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Candidate.objects.count(), initial_candidate_count - 1)