from django.urls import path
from . views import (
		users_list,
		send_friend_request,
		cancel_friend_request,
		accept_friend_request,
		delete_friend_request,
		profile_view,
	)

app_name = "friends"
urlpatterns = [
    path("", users_list, name="list"),
    path("<slug:slug>/",profile_view, name="profile"),
    path("friend_request/send/<int:pk>/", send_friend_request, name="send_friend_request"),
    path("friend_request/cancel/<int:pk>/", cancel_friend_request, name="cancel_friend_request"),
    path("friend_request/accept/<int:pk>/", accept_friend_request, name="accept_friend_request"),
    path("friend_request/delete/<int:pk>/", delete_friend_request, name="delete_friend_request"),
]
