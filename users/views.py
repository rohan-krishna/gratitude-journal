from django.shortcuts import render
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreateForm

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("users:dashboard"))
    elif request.method == 'GET':
        return render(request, "registration/register.html",{ "form" : CustomUserCreateForm})