from .models import News_Post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, DateInput


class News_PostForm(ModelForm):
    class Meta:
        model = News_Post
        fields = ['title', 'short_description', 'text', 'pub_date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Введите заголовок новости',
                'maxlength': News_Post._meta.get_field('title').max_length
            }),
            'short_description': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание новости',
                'maxlength': News_Post._meta.get_field('short_description').max_length
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите полное содержание новости...',
                'rows': '6'
            }),
            'pub_date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }
