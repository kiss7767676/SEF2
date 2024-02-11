from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.urls import reverse

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'DENTAL CLINIC SYSTEM',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

def login(request):
    if request.method == 'POST':
        # Handle login form submission
        # Assuming authentication is successful and user object is available in request.user

        # Check if user belongs to the "dentist" group
        if request.user.groups.filter(name='dentist').exists():
            print("User is a dentist")
            return render(request, 'app/dentist.html', {'title': 'Dentist Page', 'user': request.user})
        else:
            print("User is not a dentist")
            return redirect(reverse('menu'))  # Redirect to default menu for other users
    else:
        # Render login page
        print("Rendering login page")
        return render(
            request,
            'app/login.html',
            {
                'title': 'Login',
                'form': BootstrapAuthenticationForm(),  # Assuming you have a LoginForm defined
            }
        )

@login_required
def menu(request):
    check_employee = request.user.groups.filter(name='employee').exists()

    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)


@login_required
def dentist_menu(request):
    """Renders the dentist menu."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/dentist.html',
        {
            'title':'Dentist Menu',
            'year':datetime.now().year,
        }
    )
