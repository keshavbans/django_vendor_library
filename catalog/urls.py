from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name = 'authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^receipts/$', views.ReceiptsByUserListView.as_view(), name='receipts'),
    url(r'^receipt/(?P<pk>\d+)$', views.receipt_detail, name='receipt-detail'),
    url(r'^receipt/upload/$', views.upload_receipt, name='receipt-upload'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^cancel/$', views.CancelSubscription, name="cancel_subscription"),
]

urlpatterns += [
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]