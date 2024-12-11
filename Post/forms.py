from django import forms
from Post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Put an attractive and unique title...'
        }),
        error_messages={
            'unique': 'Oops! That title is already taken. How about something fresh and fun?'
        },
        label='Title:'
    )
    image_url = forms.URLField(
        help_text=" Share your funniest furry photo URL!",
        label='Post Image URL:',
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Share some interesting facts about your adorable pets...'
        }),
        label='Content:',
    )


class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']

    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'readonly': 'readonly'
        }),
        label='Title:',
    )
    image_url = forms.URLField(
        widget=forms.URLInput(attrs={
            'readonly': 'readonly'
        }),
        label='Post Image URL:'
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'readonly': 'readonly'
        }),
        label='Content:',
    )
