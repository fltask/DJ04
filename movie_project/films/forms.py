from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.utils import timezone

from .models import Films_Post


class Films_PostForm(ModelForm):
    class Meta:
        model = Films_Post
        fields = ['title', 'description', 'review']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название фильма',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание фильма',
                'rows': 3,
            }),
            'review': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отзыв на фильм',
                'rows': 5,
            }),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.pub_date = timezone.now()
        if commit:
            instance.save()
        return instance
