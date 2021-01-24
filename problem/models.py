from django.db import models

# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Problem(models.Model):
    choose = (
        ("E", "Easy"),
        ("M", "Medium"),
        ("H", "Hard"),
    )

    title = models.CharField(max_length = 100)
    description = models.TextField()
    note = models.TextField(blank = True, null = True)
    tags = models.ManyToManyField(Tags)
    level = models.CharField(max_length = 20, choices = choose)
    accuracy = models.IntegerField()
    totalSubmissions = models.IntegerField()
    sampleTc = models.IntegerField()
    totalTC = models.IntegerField()
    createdAt = models.DateField()
    memoryLimit = models.CharField(max_length = 20, null = True, blank = True)
    timeLimit = models.CharField(max_length = 20, null = True, blank = True)


    def __str__(self):
        return self.title


class UploadTC(models.Model):
    name = models.ForeignKey(to = "Problem", on_delete = models.CASCADE)
    testcases = models.FileField(upload_to = "tempTC/", blank = True, null = True)