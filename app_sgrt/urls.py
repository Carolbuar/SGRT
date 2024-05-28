from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customers/", views.customers, name="customers"),
    path("customers/customer/<int:customer_id>/", views.customer_details, name="customer"),
    path("jobs/", views.jobs, name="jobs"),
    path("jobs/job/<int:job_id>/", views.job_details, name="job"),
    path("candidates/", views.candidates, name="candidates"),
    path("candidates/candidate/<int:candidate_id>/", views.candidate_details, name="candidate"),
    
]