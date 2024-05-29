from .views import CustomerViewSet, JobViewSet, CandidateViewSet, customerList, CustomerDetail, JobList, JobDetail, CandidateList, CandidateDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'customer_viewset', CustomerViewSet)
router.register(r'job_viewset', JobViewSet)
router.register(r'candidate_viewset', CandidateViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('customerList/', CustomerList.as_view()),
    # path('customerDetail/<int:pk>/', CustomerDetail.as_view()),
    # path('jobList/', JobList.as_view()),
    # path('jobdetail/<int:pk>/', JobDetail.as_view()),
    # path('candidateList/', CandidateList.as_view()),
    # path('candidateDetail/<int:pk>/', CandidateDetail.as_view()),
    
]