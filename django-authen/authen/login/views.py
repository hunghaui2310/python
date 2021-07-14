from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

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

class ViewUser(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, req):
        return HttpResponse('<h1>Day la View User(Ban da dang nhap)</h1>')

@decorators.login_required(login_url='/login/')
def view_product(req):
    return HttpResponse('Xem san pham')


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, req):
        f = PostForm()
        context = {'fm': f}
        return render(req, 'login/add_post.html', context)

    def post(self, req):
        f = PostForm(req.POST)
        if f.is_valid():
            if req.user.has_perm('Login.add_post'):
                f.save()
            else:
                return HttpResponse('Permission Deny!')
        else:
            return HttpResponse('Form Invalid!')
        return HttpResponse('oke')