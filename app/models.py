from django.db import models

# Create your models here.


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    detailDesc = models.CharField(max_length=300)
    answerCount = models.IntegerField(null=True)
    lastModified = models.DateTimeField(auto_now=True)


class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    ansContent = models.CharField(max_length=300, null=True)
    ansDate = models.DateTimeField(auto_now=True, null=True)
    qid = models.ForeignKey('Questions', on_delete=models.CASCADE)
