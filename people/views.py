from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import NeighborHood, Profile
from .forms import ProfileForm
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def people(request):
    posts = NeighborHood.objects.all()
    print(posts)
    return render(request, 'all-people/people.html',{"posts":posts})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_images = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-projects/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-projects/search.html',{"message":message})   

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    # profiles = Profile.objects.get(user = user)
   
    return render(request,'profile.html',{"user":user})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            # profile.user = current_user
            # profile.save()

            return redirect('people')

    else:
        form = ProfileForm()
    return render(request, 'profile_form.html', {"form": form})