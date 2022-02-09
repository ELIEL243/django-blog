from django.forms import *
from .models import *


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'author', 'created_on', 'content', 'published',)
