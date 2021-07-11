from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

class LoginClass(View):
    def get(self, req):
        return render(req, "login/login.html")

    def post(self, req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        my_user = authenticate(username=username, password=password)
        if my_user is None:
            return HttpResponse("Sai ten dang nhap hoac mat khau")

        login(req, my_user)
        return render(req, 'login/success.html')

class ViewUser(View):
    def get(self, req):
        if not req.user.is_authenticated:
            return HttpResponse('Chua dang nhap')
        else:
            return HttpResponse('<h1>Day la View User(Ban da dang nhap)</h1>')