from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .form import RegistrationForm, LoginAccauntForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            accaunt = authenticate(username=username, password=password)
            login(request, accaunt)
            return redirect('home')
        else:
            context['register_form'] = form
    else:
        form = RegistrationForm()
        context['register_form'] = form
    
    return render(request, 'authentication/register.html', context)

def login_view(request):
    context = {}

    if request.POST:
        
        form = LoginAccauntForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET['next'])
                return redirect('home')
            
    else:
        form = LoginAccauntForm()
    context['login_form'] = form
    return render(request, 'authentication/login.html', context)
    
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def test(request):
    CONTEXT ={}
    return render(request,'pages/test.html', CONTEXT)


