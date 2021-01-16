from django.db import models

# Create your models here.

class Submission(models.Model):
    LANGUAGE_CODE = (
        ('CP', 'CPP'),
        ('JV', 'JAVA'),
        ('P3', 'PYTHON 3'),
        ('P2', 'PYTHON 2'),
        ('JS', 'JAVASCRIPT')
    )
    STATUS_CODE = (
        ('Q', 'QUEUED'),
        ('R', 'RUNNING'),
        ('AC', 'ACCEPTED'),
        ('CE', 'COMPILATION ERROR'),
        ('WA', 'WRONG ANSWER'),
        ('RE', 'RUNTIME ERROR')
    )
    userId = models.IntegerField(blank = False)
    problemId = models.IntegerField(blank = False)
    language = models.CharField(max_length = 2, choices = LANGUAGE_CODE)
    code = models.TextField(blank = True)
    status = models.CharField(max_length = 2, choices = STATUS_CODE)
    error = models.TextField(blank = True)
    inputGiven = models.TextField(blank = True)
    outputGen = models.TextField(blank = True) 

    def __str__(self):
        return str(self.pk)