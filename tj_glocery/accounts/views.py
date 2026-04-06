from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# ================= REGISTER =================
def register_view(request):

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # ✅ IMPORTANT LINE
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        messages.success(request, "Account Created Successfully")
        return redirect('login')

    return render(request, 'register.html')

# ================= LOGIN =================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    return redirect('home')