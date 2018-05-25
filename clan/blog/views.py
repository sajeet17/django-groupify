from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.views.generic import View
from user_login.models import UserInfo
from django.http import Http404

from .models import Post
from .forms import PostForm, SearchForm

class ProfileView(View):

	template_name = 'blog/profile.html'
	

	def get(self, request):

		if not request.user.is_authenticated:
			raise Http404

	
		queryset= UserInfo.objects.filter(user = request.user)
		#get posts in descending order
		postslists = Post.objects.filter(user= request.user).order_by('timestamp').reverse()
		
		if queryset.exists():

			user_info_context= {
			'object_list': queryset,
			'posts_list': postslists

			}

			return render(request, self.template_name, user_info_context )

		return redirect("/info/")
		
		


class CreatePostView(View):

	form_class = PostForm
	template_name= 'blog/postform.html'

	def get(self, request):

		form = self.form_class(None)

		return render(request, self.template_name, {'post_form':form})

	def post(self, request):

		form= self.form_class(request.POST or None, request.FILES or None)

		if form.is_valid():

			user_post = form.save(commit=False)
			user_post.user= request.user
			user_post.save()
			return redirect('/blog/profile/')

		return render(request, self.template_name, {'post_form':form})



class EditPostView(View):
	pass
	# form_class = PostForm
	# template_name= 'blog/postform.html'

	# def get(self, request):

	# 	instance= Post.objects.filter()
	# 	form = self.form_class(instance=instance)

class SearchFormView(View):

	form_class= SearchForm
	template_name = 'searchform.html'
	
	def post(self, request):

		searched_user = request.POST['search_result']
		#you cannot search yourself
		search_result = UserInfo.objects.filter(username__icontains=searched_user).exclude(username__iexact=request.user.username)
		
		number_of_results=len(search_result)

		context = {

		'search_result': search_result,
		'objects': number_of_results
		}

		return render(request, 'searchresults.html', context)