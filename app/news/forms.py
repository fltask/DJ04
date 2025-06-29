from .models import News_Post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput


class News_PostForm(ModelForm):
    class Meta:
        model = News_Post
        fields = '__all__'
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите полное содержание новости...'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control'}),

        }