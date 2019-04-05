from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood
@login_required(login_url='/accounts/login/')
def people_today(request):
    posts = NeighbourHood.all_posts()
    print(posts)
    return render(request, 'all-people/today-people.html',{})