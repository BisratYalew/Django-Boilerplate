from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta():
        model = Post
        ## This will be read as a tuple object because of the ','
        fields = ('post', )
