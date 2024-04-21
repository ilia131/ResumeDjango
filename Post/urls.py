from django.urls import path , include , re_path
from .views import PostViewUser




urlpatterns = [
   path('retrieveuser/', PostViewUser.as_view(), name='user-me')
]
