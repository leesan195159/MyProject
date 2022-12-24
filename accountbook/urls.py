from django.urls import path

from accountbook.views import PostAccountBook, GetAccountBook, PatchAccountBook, DeleteAccountBook, AmountDetailUrl


urlpatterns = [
    path('/post', PostAccountBook.as_view()),
    path('/get', GetAccountBook.as_view()),
    path('/patch/<int:accountbook_id>', PatchAccountBook.as_view()),
    path('/delete', DeleteAccountBook.as_view()),
    path('/url/<int:accountbook_id>', AmountDetailUrl.as_view())
]
