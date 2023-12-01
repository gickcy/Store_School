from .models import Department
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def home(request):
    departments = Department.objects.all()
    return render(request, 'home.html', {'departments': departments})




def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                django_login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('new_page')
            else:
                messages.error(request, 'Invalid username or password.')
                print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def new_page(request):
    return render(request, 'new_page.html')


def user_logout(request):
    logout(request)
    return redirect('home')

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data (save to the database, send emails, etc.)
            # You can add your custom logic here
            return render(request, 'order_confirmation.html')  # Redirect to a success page
    else:
        form = StudentForm()
    return render(request, 'order_form.html', {'form': form})




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
