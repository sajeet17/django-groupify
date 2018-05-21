from django	.urls import path
from .views import ProfileView, CreatePostView


urlpatterns=[
	path('profile/',ProfileView.as_view(), name="profile"),
    path('create-post/', CreatePostView.as_view(), name="create-post")
]