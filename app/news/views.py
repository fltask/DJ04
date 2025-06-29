from django.shortcuts import render
from .models import News_Post
from .forms import News_PostForm

# Create your views here.
def index(request):
    news = News_Post.objects.all()
    return render(request, 'news/index.html', {'news':news})

def create_news(request):
    form = News_PostForm()
    return render(request, 'news/add_new_post.html', {'form':form})