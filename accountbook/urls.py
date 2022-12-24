from django.urls import path

from accountbook.views import PostAccountBook, GetAccountBook, PatchAccountBook, DeleteAccountBook


urlpatterns = [
    path('/post', PostAccountBook.as_view()),
    path('/get', GetAccountBook.as_view()),
    path('/patch/<int:accountbook_id>', PatchAccountBook.as_view()),
    path('/delete', DeleteAccountBook.as_view())
]
