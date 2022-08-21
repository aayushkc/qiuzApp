from django.db import models

# Create your models here.
class Question(models.Model):
    question_title = models.TextField(max_length=250)
    option_A = models.CharField(max_length=100)
    option_B = models.CharField(max_length=100)
    option_C = models.CharField(max_length=100)
    option_D = models.CharField(max_length=100)
    correct_ans = models.CharField(max_length=100)
    def __str__(self):
        return self.question_title
        
    class Meta:
        db_table = 'tbl_question_answer'


#USER Models 
class AppUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'tbl_Users'

        