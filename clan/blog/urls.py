from django	.urls import path
from .views import ProfileView, CreatePostView, SearchFormView


urlpatterns=[
	path('profile/',ProfileView.as_view(), name="profile"),
    path('create-post/', CreatePostView.as_view(), name="create-post"),
    path('search/', SearchFormView.as_view(), name="search-result")
]