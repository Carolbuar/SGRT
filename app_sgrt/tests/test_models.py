from django.test import TestCase
from ..models import Customer, Job, Candidate

class CustomerModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Test Customer",
            email="testcustomer@example.com",
            website="http://example.com",
            address="123 Test St",
            phone="1234567890",
            representative_name="John Doe"
        )

        self.job1 = Job.objects.create(
            name="Job 1",
            status="open",
            customer=self.customer,
            description="Description for Job 1",
            location="Location 1"
        )

        self.job2 = Job.objects.create(
            name="Job 2",
            status="closed",
            customer=self.customer,
            description="Description for Job 2",
            location="Location 2"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.customer), self.customer.name)

    def test_qtt_open_jobs(self):
        self.assertEqual(self.customer.qtt_open_jobs(), 1)

    def test_open_jobs(self):
        open_jobs = self.customer.open_jobs()
        self.assertEqual(open_jobs.count(), 1)
        self.assertEqual(open_jobs.first().name, "Job 1")

class JobModelTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Test Customer",
            email="testcustomer@example.com",
            website="http://example.com",
            address="123 Test St",
            phone="1234567890",
            representative_name="John Doe"
        )

        self.job = Job.objects.create(
            name="Job 1",
            status="open",
            customer=self.customer,
            description="Description for Job 1",
            location="Location 1"
        )

        self.candidate1 = Candidate.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="janedoe@example.com",
            resume="path/to/resume1.pdf",
            skills="Skill 1, Skill 2"
        )

        self.candidate2 = Candidate.objects.create(
            first_name="John",
            last_name="Smith",
            email="johnsmith@example.com",
            resume="path/to/resume2.pdf",
            skills="Skill 3, Skill 4"
        )

        self.job.candidates.add(self.candidate1, self.candidate2)

    def test_string_representation(self):
        self.assertEqual(str(self.job), self.job.name)

    def test_qtt_candidatesforjob(self):
        self.assertEqual(self.job.qtt_candidatesforjob(), 2)

class CandidateModelTest(TestCase):

    def setUp(self):
        self.candidate = Candidate.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="janedoe@example.com",
            resume="path/to/resume1.pdf",
            skills="Skill 1, Skill 2"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.candidate), f"{self.candidate.first_name} {self.candidate.last_name}")