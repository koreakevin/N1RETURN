from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm, CommentForm
from .models import Blog, Comment
from django.views.generic. base import TemplateView
# Create your views here.

class MainpageView(TemplateView):
        template_name = 'layout.html'

def layout(request):
    return render(request, 'layout.html')

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/velvet/home/')

def blogform(request, blog=None):
    if request.method =='POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'new.html', {'form':form})

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)


def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')

def comment_new(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article_id = blog
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("home")
    else:
        form = CommentForm()
        return render(request, "detail.html", {"form": form})

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect("home")


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect("home")
    else:
        form = CommentForm(instance=comment)
        return render(request, "detail.html", {"form": form})