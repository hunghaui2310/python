from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

# function base view
def index(request):
    my_name = "HungNN"
    taisan = ["Dien thoai", "May tinh", "May bay"]
    return render(request, "polls/index.html", {"name": my_name, "taisan": taisan})

def ham1(req):
    return HttpResponse("<h1>Ham linh tinh</h1>")

def showAllQuestions(req):
    list_question = Question.objects.all()
    context = {"questions": list_question}
    return render(req, "polls/questions.html", context)

def showOneQuestion(req):
    question = get_object_or_404(Question, pk=1)
    return render(req, "polls/questions.html", {"question": question})


def detailView(req, question_id):
    question = Question.objects.get(pk=question_id)
    return render(req, "polls/detail_question.html", {"question": question})

def submit(req, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = req.POST['choice']
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("NO CHOICE")
    c.vote = c.vote + 1
    c.save()
    return render(req, "polls/result.html", {"question": q})