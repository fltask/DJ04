from django.shortcuts import render, redirect
from .models import News_Post
from .forms import News_PostForm

# Create your views here.
def index(request):
    news = News_Post.objects.all()
    return render(request, 'news/index.html', {'news':news})

def create_news(request):
    if request.method == 'POST':
        form = News_PostForm(request.POST)
        if form.is_valid():
            news_post = form.save(commit=False)
            if request.user.is_authenticated:
                news_post.author = request.user
            news_post.save()
            return redirect('news:news_home')
        # form.errors уже содержит ошибки
    else:
        form = News_PostForm()

    # Получаем значения maxlength из модели
    title_max_length = News_Post._meta.get_field('title').max_length
    description_max_length = News_Post._meta.get_field('short_description').max_length

    return render(request, 'news/add_new_post.html', {
        'form': form,
        'title_max_length': title_max_length,
        'description_max_length': description_max_length
    })
