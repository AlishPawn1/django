from django.shortcuts import render, redirect
from profiles.models import UserProfile
from profiles.forms import ProfilesModelForm

def profile_create_view(request):
    if request.method == "GET":
        form = ProfilesModelForm()
        return render(request, "profile/create.html", {"form": form})
    elif request.method == "POST":
        form = ProfilesModelForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile/list.html')
    return render(request, "profile/create.html", {"form": form})
