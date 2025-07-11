from django.shortcuts import render, redirect
from .models import Films_Post
from .forms import Films_PostForm

# Create your views here.
def index(request):
    films = Films_Post.objects.all().order_by('-pub_date')
    return render(request, 'films/index.html', {'films': films})

def create_review(request):
    if request.method == 'POST':
        form = Films_PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films:films_home')
    else:
        form = Films_PostForm()

    return render(request, 'films/add_movie_review.html', {'form': form})
