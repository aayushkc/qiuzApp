
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from .forms import CreateQuestion, LoginForm, RegisterForm
from .models import Question, AppUser
import random
# Create your views here.

#USER views 
def LoginUser(request):
    if request.method == 'POST':
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')
        db_data = AppUser.objects.get(email = req_email)
        if req_password == db_data.password:
            return redirect('quiz.welcome')
        else:
            return redirect('quiz.login')
    else:
        login_form = LoginForm()
        template = 'users/login.html'
        context = {
            'login_form':login_form
        }
        return render(request, template, context)

def RegisterUser(request):
    if request.method == 'POST':
        user_register = RegisterForm(request.POST)
        if user_register.is_valid():
            user_register.save()
            return redirect('quiz.login')
    else:
        register_form = RegisterForm()
        template = 'users/register.html'
        context ={
            'reg_form':register_form
        }
        return render(request, template, context)


#USER View Pages 
def user_welcome(request):
    if request.method == 'POST':
        element = Question.object.get(pk=1)
        return redirect('quiz.user.question', pk = element.id)
    else:
        template = 'userpages/welcome.html'
        return render(request, template)


def user_question(request):
    questions_list = list(Question.objects.all())
    random.shuffle(questions_list)
    questions = questions_list[:3]
    context = {
        'questions':questions
    }
    template = 'userpages/question.html'
    return render(request, template, context)

def user_answer(request):
    questions = Question.objects.all()
    score = 0
    correct_answer = 0
    for question in questions:
       user_ans =  request.POST.get(question.question_title)

       if question.correct_ans == user_ans:
        score += 10
        correct_answer += 1
    return render(request, 'userpages/result.html', context = {
            'score': score,
            'correct_answer':correct_answer
     })

def user_show_answer(request):
    answers = Question.objects.values_list('correct_ans')
    template = 'userpages/answers.html'
    context = {
        'answers': answers
    }
    return render(request, template, context)

def questions(request):
    questions = Question.objects.all
    context = {
        'title':'Add questions',
        'body_title':'Questions for the quiz:',
        'questions':questions
    }
    template = 'questions/index.html'
    return render(request, template, context)
def add_question(request):
    if request.method == "POST":
        form_data = CreateQuestion(request.POST)
        if form_data.is_valid():
            form_data.save()
            return redirect('quiz.questions') 
        else:
            create_question = CreateQuestion()
            template = 'questions/addquestion.html'
            context = {
                'title':'Add question',
                'body_title':'Add question for quiz',
                'form': create_question
            }
            return render(request, template, context) 
    else:
        create_question = CreateQuestion()
        template = 'questions/addquestion.html'
        context = {
            'title':'Add question',
            'body_title':'Add question for quiz',
            'form': create_question
        }
        return render(request, template, context)
def question_update(request):
    if request.method == 'POST':
        question = Question.objects.get(id = request.POST.get('id'))
        question.question_title = request.POST.get('question_title')
        question.option_A = request.POST.get('option_A')
        question.option_B = request.POST.get('option_B')
        question.option_C = request.POST.get('option_C')
        question.option_D = request.POST.get('option_D')
        question.correct_ans = request.POST.get('correct_ans')
        question.save()
        questions = Question.objects.all()
        template = 'questions/index.html'
        context = {
            'questions':questions
        }
        return render(request, template, context)
    else:
        create_form = CreateQuestion()
        template = 'questions/addquestion.html'
        context = {
            'form': create_form
        }
        return render(request, template, context)
def question_edit(request, id):
    question = Question.objects.get(id = id)
    template = 'questions/edit.html'
    context ={
        'question':question
    }
    return render(request, template, context)

def question_delete(request, id):
    question = Question.objects.get(id = id)
    question.delete()
    questions = Question.objects.all()
    template = 'questions/index.html'
    context = {
        'questions': questions
    }
    return render(request, template, context)