from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from user.models import Profession, Contact


# my views
@login_required(login_url="/login/")
def home(request):
    context = {}
    userreq                     = request.user
    carusel                     = Carusel.objects.filter(user=userreq)[:7]
    context['carusels']         = carusel
    professions                 = Profession.objects.filter(user=userreq)[:3]
    context['professions']      = professions
    works                       = Work.objects.filter(user=userreq)
    context['works']            = works
    partners                    = Partner.objects.filter(user=userreq)[:3]
    context['partners']         = partners
    contacts                    = Contact.objects.filter(user=userreq)
    context['contacts']         = contacts

    return render(request, 'index.html', context)
