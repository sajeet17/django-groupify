from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# authenticate takes username and password and verifies if the username and password exists
# login attaches a session id 
from django.views.generic import View
from .forms import UserForm

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
					#now you can address the user as
					#request.user.username or sth like that
					#also to redirect after login
					return redirect("/admin")

	#if login is not valid just give blank fall
		return render(request, self.template_name, {'form':form})	




