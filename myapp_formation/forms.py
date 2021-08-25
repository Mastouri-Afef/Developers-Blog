from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
    #here we will say which model we will, work with and witch field we will display
        model = Comment
        #after that moving to the views file to add the file
        fields = ('content', )   
