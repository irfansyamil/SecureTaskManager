from django import forms
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator
from .models import Task

class TaskForm(forms.ModelForm):
    # Strict regex whitelist: Only allows alphanumeric characters, spaces, hyphens, and underscores.
    # This prevents users from injecting HTML tags like <script> (XSS protection).
    alphanumeric_spaces_regex = RegexValidator(
        regex=r'^[a-zA-Z0-9\s\-_.,!?]+$',
        message="Invalid characters used. Only letters, numbers, spaces, and basic punctuation are allowed."
    )

    title = forms.CharField(
        validators=[
            MinLengthValidator(3, message="Title must be at least 3 characters long."),
            MaxLengthValidator(100, message="Title cannot exceed 100 characters."),
            alphanumeric_spaces_regex
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter secure task title...'
        })
    )

    description = forms.CharField(
        required=False,
        validators=[
            MaxLengthValidator(500, message="Description cannot exceed 500 characters."),
            alphanumeric_spaces_regex
        ],
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter task details safely...'
        })
    )

    class Meta:
        model = Task
        fields = ['title', 'description']