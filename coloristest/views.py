from django.shortcuts import render
from .forms import PostForm
from .models import Post

def notes(request):
    posts = Post.objects.order_by('text')
    if request.method == "POST":
        form = PostForm(request.POST)
        post = form.save()
        post.save()
    else:
        form = PostForm()
    return render(request, 'coloristest/notes.html', {'form': form, 'posts': posts})
    
