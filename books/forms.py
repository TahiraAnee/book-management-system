from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description", "published_year"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "placeholder": "Write Book Title...",
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "w-full p-2 border rounded",
                    "placeholder": "Enter Authors Name...",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full p-3 border rounded",
                    "placeholder": "Write Description...",
                }
            ),
            "published_year": forms.TextInput(
                attrs={
                    "class": "w-full p-3 border rounded",
                    "placeholder": "Write Publishing Year...",
                }
            ),
        }
