from django.http import HttpResponseRedirect, HttpResponse

from .forms import UserForm,UserUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout as my_logout, login as my_login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, auth


def index(request):

    if 'username' in request.session:

        return render(request, "testapp/index.html",{'username': request.session['username']} )

    return render(request, "testapp/index.html")


def login(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:

        my_login(request, user)


        request.session['username'] = username
        print(user.password)
        return render(request, 'testapp/index.html')

    else:

        form = AuthenticationForm()

    return render(request, "testapp/login.html", {'form' : form})


def signup(request):

    if request.method == 'POST':

        form = UserForm(request.POST)

        if form.is_valid():

            form.save()
            print("user created.")
            return render(request, 'testapp/index.html')

        else:

            context = 'not validated'
            return render(request, 'testapp/signup.html', {'form': form, 'context': context})

    form = UserForm()
    return render(request, 'testapp/signup.html', {'form': form})


def logout(request):

    my_logout(request)

    return render(request, "testapp/index.html")


@login_required(login_url='/testapp/login/')  # redirect when user is not logged in
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('profile')
    else:

        form = UserUpdateForm(instance=request.user)
        return render(request, "testapp/profile.html", { 'form' : form})

def password_reset(request):

    if request.method=='POST':

        render(request, password_reset)