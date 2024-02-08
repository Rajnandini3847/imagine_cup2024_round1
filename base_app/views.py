from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth  import authenticate,  login, logout
# views.py
from django.shortcuts import render, redirect
from .models import Job, Application
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def landing_page(request):
    return render(request, 'landing_page.html')

def Register(request):
    if request.method != "POST":
        return render(request, "register.html")
    username = request.POST['username']
    email = request.POST['email']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 != password2:
        messages.error(request, "Passwords do not match.")
        return redirect('/register')

    user = User.objects.create_user(username, email, password1)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    return render(request, 'frontpage.html')

def Login(request):
    if request.method != "POST":
        return render(request, "frontpage.html")
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        messages.success(request, "Successfully Logged In")
        return redirect('/')
    else:
        messages.error(request, "Invalid Credentials")
    return render(request ,'after_login.html')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')

def restaurants(request):
    return render(request, 'restaurants_map.html')

def hospitals(request):
    return render(request, 'hospitals_map.html')

def schools_and_colleges(request):
    return render(request, 'schools_and_colleges.html')



@login_required
def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, 'job_detail.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
    if request.method == 'POST':
        job = Job.objects.get(id=job_id)
        application_text = request.POST.get('application_text')

        Application.objects.create(
            job=job,
            applicant=request.user.userprofile,
            message=application_text
        )

        messages.success(request, 'Application submitted successfully!')
        return redirect('job_list')

    return render(request, 'apply_for_job.html', {'job_id': job_id})
