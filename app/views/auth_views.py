from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages

class AuthView(View):
    def get(self, reqeust):
        if reqeust.user.is_authenticated:
            return redirect('index')
        return render(reqeust, 'app/login.html', {})
    
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        email = request.POST.get('email','')
        password = request.POST.get('password', '')
        if email == '' or password  == '':
            messages.error(request, 'Email and password is required')
            return redirect('login')
        auth_user = authenticate(request, username=email, password = password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('index')
        messages.error(request, 'Your credentails is incorrect')
        return redirect('login')

class LogoutView(View):
    def get(self ,request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('index')
