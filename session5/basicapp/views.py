from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from basicapp.forms import UserProfileInfoForm, Userform


def index(request):
    return render(request, 'basicapp/index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == "POST":
        user_form = Userform(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pics' in request.FILES:
                profile.profile_pic = request.FILES['profile_pics']

            profile.save()
            registered = True
        else:
            print("failure")

    else:
        user_form = Userform()
        profile_form = UserProfileInfoForm()

    return render(request, 'basicapp/registration.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        userauthentication = authenticate(username=username, password=password)
        if userauthentication:
            if userauthentication.is_active:
                login(request, userauthentication)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User is not active!!!1")
        else:
            print("User credentials are not valid")
            return HttpResponse("You are not valid user!!!")
    else:
        return render(request, 'basicapp/login.html')
