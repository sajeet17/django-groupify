from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:

		model = Post
		fields= ['title','status', 'picture']

class SearchForm(forms.Form):

	search_field = forms.CharField(max_length=30)
		
