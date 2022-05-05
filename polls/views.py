from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Article, Comment
from django.utils import timezone
from django.urls import reverse
from django.http import JsonResponse

import os
from django.conf import settings


# Create your views here.
def index(request):
    article_list = Article.objects.order_by('-pub_date')
    context = {'article_list': article_list}
    return render(request, 'index.html', context)


def detail(request):
    return render(request, 'detail.html', {})


def result(request, article_id):
    article = Article.objects.get(pk=article_id)

    return render(request, 'result.html', {'article': article})


def vote(request):
    try:
        Article.objects.get(title=request.POST['title'])
        return render(request, 'detail.html',
                      {'title': request.POST['title'], 'error_message': "This title already exit!"})

    except Article.DoesNotExist:
        title = request.POST['title']
        content = request.POST['content']
        if title == '':
            return render(request, 'detail.html', {'title_empty': "title can't be empty!"})
        elif content == '':
            return render(request, 'detail.html', {'content_empty': "content can't be empty!"})
        else:
            photo = request.FILES.get('photo')
            a = Article(title=title, content=content, pub_date=timezone.now(), photo=photo)
            a.save()

            return HttpResponseRedirect(reverse('polls:result', args=(a.id,)))


def delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('/polls')


def reply(request):
    print(request.POST)
    article_id = request.POST.get('article_id')
    c_content = request.POST.get('c_content')
    a.comment_set.create(c_content=c_content)

    return HttpResponse('ok')

def edit(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'edit.html', {'article': article})


def save_again(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.title = request.POST['title']
    article.content = request.POST['content']
    article.save()
    return HttpResponseRedirect(reverse('polls:result', args=(article.id,)))
