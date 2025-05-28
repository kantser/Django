from django.shortcuts import render, redirect
from .models import Service, Project, TeamMember
from .forms import ContactForm

def home(request): # type: ignore
    services = Service.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)[:4]
    team_members = TeamMember.objects.all()
    
    if request.method == 'POST': # type: ignore
        form = ContactForm(request.POST) # type: ignore
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    
    context = { # type: ignore
        'services': services,
        'projects': featured_projects,
        'team': team_members,
        'form': form,
    }
    return render(request, 'main/home.html', context) # type: ignore

def contact(request): # type: ignore
    if request.method == 'POST': # type: ignore
        form = ContactForm(request.POST) # type: ignore
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form}) # type: ignore

def contact_success(request): # type: ignore
    return render(request, 'main/contact_success.html') # type: ignore
