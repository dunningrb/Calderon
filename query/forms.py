from django import forms
from query.models import Post


class QueryBasicForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Write a post....',
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

