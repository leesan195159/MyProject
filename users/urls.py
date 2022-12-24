from django.urls import path

from users.views import SignIn, LogIn

urlpatterns = [
    path('/signin', SignIn.as_view()),
    path('/login', LogIn.as_view())
]
