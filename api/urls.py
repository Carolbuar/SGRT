from . import views
from .views import (CustomerViewSet, JobViewSet, CandidateViewSet, FilteredJobListByCustomer, FilteredJobListByStatus, FilteredJobListByLocation)
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'customer', CustomerViewSet)
router.register(r'job', JobViewSet)
router.register(r'candidate', CandidateViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('customer-list/', views.customerList, name="customer_list"),
    path('customer-detail/<int:pk>/', views.customerDetail, name="customer_detail"),
    path("customer-create/", views.customerCreate, name="customer_create"),
    path('customer-update/<int:pk>/', views.customerUpdate, name="customer_update"),
    path('customer-delete/<int:pk>/', views.customerDelete, name="customer_delete"),
    path('job-list/', views.jobList, name="job_list"),
    path('job-detail/<int:pk>/', views.jobDetail, name="job_detail"),
    path('job-create/', views.jobCreate, name="job_create"),
    path('job-update/<int:pk>/', views.jobUpdate, name="job_update"),
    path('job-delete/<int:pk>/', views.jobDelete, name="job_delete"),
    path('candidate-list/', views.candidateList, name="candidate_list"),
    path('candidate-detail/<int:pk>/', views.candidateDetail, name="candidate_detail"),
    path('candidate-create/', views.candidateCreate, name="candidate_create"),
    path('candidate-update/<int:pk>/', views.candidateUpdate, name="candidate_update"),
    path('candidate-delete/<int:pk>/', views.candidateDelete, name="candidate_delete"),
    path("add-candidate-to-job/<int:candidate_id>/<int:job_id>/", views.addCandidateToJob, name="add_candidate_to_job"),
    path("candidates-applied-to-job/<int:job_id>/", views.candidatesAppliedToJob, name="candidates_applied_to_job"),
    path("filtered-job-list-location/", FilteredJobListByLocation.as_view(), name="filtered_job_list_location"),
    path("filtered-job-list-status/", FilteredJobListByStatus.as_view(), name="filtered_job_list_status"),
    path("filtered-job-list-customer/", FilteredJobListByCustomer.as_view(), name="filtered_job_list_customer"),
]