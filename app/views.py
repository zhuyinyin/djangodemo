from django.shortcuts import render, redirect
from app.models import Questions, Answers
import datetime


# Create your views here.


def index(request):
    if request.method == 'GET':
        questions = Questions.objects.all()

        return render(request, 'index.html', locals())


def quest(request):
    if request.method == 'GET':
        return render(request, 'quest.html')
    if request.method == 'POST':

        title = request.POST.get('title')
        detail = request.POST.get('detail')
        if title == ''or detail == '':
            msg ='yes'
            return render(request, 'quest.html', locals())
        Questions.objects.create(title=title, detailDesc=detail, answerCount=0, lastModified=datetime.datetime.now())
        return redirect('/index')


def answ(request, q_id):
    if request.method == "GET":
        questions = Questions.objects.filter(id=q_id).first()
        answers = Answers.objects.filter(qid_id=q_id)
        return render(request, 'answ.html', locals())
    if request.method == 'POST':
        questions = Questions.objects.filter(id=q_id).first()
        answers = Answers.objects.filter(qid_id=q_id)
        ansData = request.POST.get('my_ans')
        if ansData == '':
            msg = 'yes'
            return render(request, 'answ.html', locals())
        ansCount = Questions.objects.filter(id=q_id).first().answerCount
        # 回答次数加一
        ansCount += 1
        Answers.objects.create(ansContent=ansData, ansDate=datetime.datetime.now(), qid_id=q_id)
        # 数据传给页面
        answers = Answers.objects.filter(qid_id=q_id)
        questions = Questions.objects.filter(id=q_id).first()
        # 更新次数
        Questions.objects.filter(id=q_id).update(answerCount=ansCount)
        return render(request, 'answ.html', locals())