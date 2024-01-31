from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

from .models import Article
from .forms import ArticleForm



class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/accounts/login'

    def form_valid(self, form):
        return super().form_valid(form)















# Create your views here.

@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, "app/article_list.html", {'articles': articles})

@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "app/article_detail.html", {'article': article})

@login_required
def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            return redirect("article_detail", pk=article.pk)
        
    else:
        form = ArticleForm()
    return render(request, "app/article_edit.html", {'form': form})

@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article_detail", pk=article.pk)
        
    else:
        form = ArticleForm(instance=article)
    return render(request, "app/article_edit.html", {'form': form})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect("article_list")