import operator

from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import DeleteView
from legacy import reduce
from django.core.mail import send_mail

from users.models import BlogUser
from .forms import NewsForm
from .models import News


def index(request):
    news = News.objects.all().order_by('-data_publikacji')
    context = {'news': news,}
    return render(request, 'index.html', context)

def author(request,name):
    autor=get_object_or_404(BlogUser,pk=name)
    news = News.objects.filter(autor__pk=name)
    return render(request, 'author.html', {'autor' : autor, 'news' : news})

def news_show_detail(request, pk):
    curr_post = get_object_or_404(News,pk=pk)
    return render(request, 'news.html', {'curr_post' : curr_post},)


def searching(request):
    search_list=News.objects.all()
    print(search_list)
    search=request.GET.get("q")
    if search:
        query_list = search.split()
        search_list=search_list.filter(
                reduce(operator.and_,
                       (Q(tytul__icontains=q) for q in query_list)
            ))

        print(search_list)
    return render(request,'news_search.html',{'curr_post':search_list})


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.autor=request.user
            post.save()
            form.save_m2m()
            users = BlogUser.objects.all()
            for x in users:
                if not x.is_superuser:
                    send_mail('Nowy wpis',
                              'Na blogu dodano wpis o tytule: '+post.tytul+'\n'+'link: 127.0.0.1:8000/news/%i/'%post.pk,
                              'blognotify@gmail.com',
                              [x.email],
                              )
            return redirect('news_show_detail', pk=post.pk)
    else:
        form = NewsForm()
    return render(request, 'add_news_form.html', {'form' : form})


class DeleteNews(DeleteView):
    model = News
    template_name = 'delete_news.html'
    success_url = '/news/'
