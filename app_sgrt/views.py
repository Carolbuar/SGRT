from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Customer, Job, Candidate
from .forms import CustomerForm, JobForm, CandidateForm
from django.contrib.auth.decorators import login_required


def index(request):
    template = loader.get_template('index.html')
    context = {
        'tittle': 'SGRT - Home'
    }
    return HttpResponse(template.render(context, request))

def customers(request):
    form = CustomerForm()
    customers = Customer.objects.all()
    template = loader.get_template('customers.html')
    context = {
        'customers': customers,
        'tittle': 'SGRT - Customers',
        'form': form
    }
    return HttpResponse(template.render(context, request))

def customer_details(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    template = loader.get_template('customer_details.html')
    context = {
        'customer': customer,
        'tittle': 'SGRT - Customer Details'
    }
    return HttpResponse(template.render(context, request))


def jobs(request):
    form = JobForm()
    jobs = Job.objects.all()
    template = loader.get_template('jobs.html')
    context = {
        'jobs': jobs,
        'tittle': 'SGRT - Jobs',
        'form': form
    }
    return HttpResponse(template.render(context, request))

def job_details(request, job_id):
    job = Job.objects.get(id=job_id)
    template = loader.get_template('job_details.html')
    context = {
        'job': job,
        'tittle': 'SGRT - Job Details'
    }
    return HttpResponse(template.render(context, request))

def candidates(request):
    form = CandidateForm()
    candidates = Candidate.objects.all()
    template = loader.get_template('candidates.html')
    context = {
        'candidates': candidates,
        'tittle': 'SGRT - Candidates',
        'form': form
    }
    return HttpResponse(template.render(context, request))

def candidate_details(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    applied_jobs = candidate.applied_jobs.all()
    template = loader.get_template('candidate_details.html')
    context = {
        'candidate': candidate,
        'applied_jobs': applied_jobs,
        'tittle': 'SGRT - Candidate Details'
    }
    return HttpResponse(template.render(context, request))


@login_required
def staff(request):
    user = request.user
    if user.is_staff:
        context = {'is_admin': True}
    else:
        context = {'is_admin': False}

    return render(request, 'my_template.html', context)