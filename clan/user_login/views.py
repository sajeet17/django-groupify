from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# authenticate takes username and password and verifies if the username and password exists
# login attaches a session id 
from django.views.generic import View
from .forms import UserForm, UserInfoForm, LoginForm
from .models import UserInfo



def logout_handler(request):
	logout(request)
	return redirect("/")

class LoginHandler(View):
	form_class= LoginForm
	template_name='login_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'login_form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user= authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					request.session['user_username'] = user.username
					return redirect("/profile/")

		return render(request, 'failed_login.html', {'login_form':form})



class UserFormView(View):
	form_class = UserForm
	template_name = 'register_form.html'


	#this is the best way to do it... define get and post functions
	
	#if there is a get request that mean user is requesting the form, so display blank form

	def get(self, request):

		#use the UserForm with no context blank data
		form = self.form_class(None)
		return render(request, self.template_name,{'form': form})

	#process form data	
	def post(self, request):
		#now the request.POST contains all the data for post so 
		#request.POST saves all the data for post request
		form = self.form_class(request.POST)
		#pass data to validate itself, unless errors

		if form.is_valid():
			#take the info and store it inside database, but validate before that
			
			user =  form.save(commit = False)
			#this user object will take the data filled in the form
			#commit=false will not save it to the user database, store it locally only

			#cleaned (normalized) data

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			#to set username you can use
			# user.username="tom"
			#but since password will give hash values
			# to set a password
			user.set_password(password)
			#to save the user after setting everything correctly
			user.save()

			#returns User objects if credentials are correct
			user= authenticate(username=username, password=password)

			if user is not None:
				#to check if disabled or any status or banned
				

				if user.is_active:
					

					#now to log them in
					login(request, user)
					request.session['user_username'] = user.username
					#now you can address the user as
					#request.user.username or sth like that
					#also to redirect after login
					return redirect("/info/")

	#if login is not valid just give blank form
		return render(request, self.template_name, {'form':form})	




class UserInfoView(View):

	form_class= UserInfoForm
	template_name="userinfo_form.html"
	
	def get(self, request):
		username = request.session['user_username']

		try:
		    user_profile_data = UserInfo.objects.get(username = username)
		
		except Exception:
		    user_profile_data = None

		form= self.form_class(instance = user_profile_data)
		

		return render(request, self.template_name,{'form':form,'user':username})

	
	def post(self, request):

		username = request.session['user_username']

		user_profile_data = UserInfo.objects.filter(username = username)

		form = self.form_class(request.POST or None, request.FILES or None)


		if form.is_valid():

			user_info = form.save(commit=False)

			first_name      = form.cleaned_data['first_name']
			last_name       = form.cleaned_data['last_name']
			age			    = form.cleaned_data['age']
			description     = form.cleaned_data['description']
			profile_picture = form.cleaned_data['profile_picture']
			username        = form.cleaned_data['username']

			if user_profile_data.exists():
				if profile_picture:

					user_profile_data.update(first_name=first_name, last_name=last_name, age=age, description=description, profile_picture=profile_picture)
				else:

					user_profile_data.update(first_name=first_name, last_name=last_name, age=age, description=description)

			else:

				user_info.save()

			return redirect("/profile/")
		
		return render(request, self.template_name, {'form':form, 'user':username})


class ProfileView(View):

	template_name = 'profile.html'
	

	def get(self, request):

		username = request.session['user_username']

		if username is not None:
			queryset= UserInfo.objects.filter(username = username)
			
			if queryset.exists():

				user_info_context= {
				'object_list': queryset
				}

				return render(request, self.template_name, user_info_context )

			return redirect("/info/")
		
		return render(request, '404error.html', {})
