from django.shortcuts import render


# Create your views here.
from .models import Book, Author, BookInstance, Genre, Receipt
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_visits': num_visits},
    )

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    model = Book
class AuthorListView(generic.ListView):
    model = Author
class AuthorDetailView(generic.DetailView):
    model = Author
class ReceiptListView(LoginRequiredMixin, generic.ListView):
    model = Receipt
class ReceiptDetailView(LoginRequiredMixin, generic.DetailView):
    model = Receipt





class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

from django.contrib.auth.decorators import permission_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import RenewBookForm

@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst=get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['/']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    return render(request, 'catalog/book_renew_librarian.html', {'form': form, 'bookinst':book_inst})

from .forms import ImageUploadForm
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required()
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk = pk)
    name = receipt.name
    image = receipt.receipt_image
    user = receipt.owner
    updated = receipt.updated_at

    return render ( request,
                    'receiptd.html',
                    context=
                    {'name' : name,
                     'image' : image,
                     'user' : user,
                     'updated' : updated}
    )


@login_required
def upload_receipt(request):
    """
    View function for renewing a specific BookInstance by librarian
    """
    if request.user.is_authenticated:
            # If this is a POST request then process the Form data
        if request.method == 'POST':
            # Create a form instance and populate it with data from the request (binding):
            form = ImageUploadForm(request.POST, request.FILES)

            # Check if the form is valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                m = Receipt()
                m.name = form.cleaned_data['name']
                m.updated_at = form.clean_billed_date()
                m.owner = request.user
                m.receipt_image = request.FILES['image']
                print(m.receipt_image)
                m.save()
                return HttpResponse('receipt upload success')

                # redirect to a new URL:
            return HttpResponseForbidden('allowed only via POST')

        else:
            form = ImageUploadForm
    return render(request, 'catalog/upload_receipt.html', {'form': form,})
""""
def upload_receipt(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            m = Receipt()
            m.name = form.cleaned_data['name']
            m.updated_at = form.clean_billed_date()
            m.owner = form.c
            m.receipt_image = form.cleaned_data['image']
            m.save()
            return HttpResponse('image upload success')
    return HttpResponseForbidden('allowed only via POST')
"""
class ReceiptsByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Receipt
    template_name = 'catalog/receipts_list_uploaded_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Receipt.objects.filter(owner=self.request.user).order_by('updated_at')

def terms(request):
    """
    View function for Terms and condition of the site.
    """
    # Generate counts of some of the main objects
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'terms.html',
    )


@login_required
def CancelSubscription(request):
    """
    View function for Terms and condition of the site.

    # Generate counts of some of the main objects
    # Render the HTML template index.html with the data in the context variable
    """
    """if request.user.is_authenticated:
        if request.method == 'POST':
            form =
            if form.is_valid():
            """

    return render(
        request,
        'cancel_subscription.html',
    )
