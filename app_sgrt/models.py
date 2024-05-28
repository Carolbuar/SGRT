from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    representative_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def qtt_open_jobs(self):
        return self.jobs.filter(status='open').count()
    
    def open_jobs(self):
        return self.jobs.filter(status='open')
    
class Job(models.Model):
    STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='jobs')
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def qtt_candidatesforjob(self):
        return self.candidates.count()

class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    resume = models.FileField(upload_to='resumes/')
    skills = models.TextField()
    applied_jobs = models.ManyToManyField(Job, related_name='candidates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"