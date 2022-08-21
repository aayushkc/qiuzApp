
from django.urls import path
from . import views

urlpatterns = [
    path('add-question/', views.add_question, name='quiz.add'),
    path('questions/', views.questions, name = 'quiz.questions'),
    path('questions/update/<int:id>', views.question_edit, name='question.edit'),
    path('question/update', views.question_update, name = 'question.update'),
    path('questions/delete/<int:id>', views.question_delete, name='question.delete'),
    path('user/register', views.RegisterUser, name='quiz.register'),
    path('user/login', views.LoginUser, name='quiz.login'),
    path('user/welcome', views.user_welcome, name='quiz.welcome'),
    path('user/question', views.user_question, name='quiz.user.question'),
    path('user/result', views.user_answer, name='quiz.user.answer'),
    path('user/showanswer', views.user_show_answer, name='quiz.show.answer')
]