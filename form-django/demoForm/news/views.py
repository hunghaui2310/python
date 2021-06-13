from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View

# Create your views here.

def index(req):
    return HttpResponse('Chao')

def addPost(req):
    f = PostForm()
    return render(req, "news/add_new.html", {"f": f})

def saveNew(req):
    if req.method == 'POST':
        data = PostForm(req.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('Luu thanh cong')
        else:
            return HttpResponse('Luu that bai, du lieu khong hop le')
    else:
        return HttpResponse('Bad request 400')

def emailView(req):
    f = SendEmail()
    return render(req, 'news/email.html', {'f': f})

def receivedEmail(req):
    if req.method == 'POST':
        mailForm = SendEmail(req.POST)
        if mailForm.is_valid():
            title = mailForm.cleaned_data['title']
            content = mailForm.cleaned_data['content']
            email = mailForm.cleaned_data['email']
            cc = mailForm.cleaned_data['cc']
            context = {"title": title, 'cc': cc, "content": content, "email": email}
            context2 = {"f": mailForm}
            # mailForm.save()
            return render(req, "news/print_email.html", context2)
        else:
            return HttpResponse('Luu that bai, du lieu khong hop le')
    else:
        return HttpResponse('Bad request 400')

# class  base view
class IndexClass(View):
    def get(self, req):
        return HttpResponse("This is class base view")


class SavePost(View):
    def get(self, req):
        f = PostForm()
        return render(req, "news/add_new.html", {"f": f})

    def post(self, req):
        f = PostForm(req.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("Luu thanh cong")
        else:
            return HttpResponse("Invalid!")