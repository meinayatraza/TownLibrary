from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Book, Category
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Home page - Select section
def home(request):
    return render(request, 'home.html')

# Book list by section with search and filter
def book_list(request, section):
    # Get all books for this section
    books = Book.objects.filter(section=section)
    
    # Get all categories for sidebar
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        books = books.filter(
            Q(title__icontains=search_query) |
            Q(author__icontains=search_query) |
            Q(isbn__icontains=search_query)
        )
    
    # Category filter
    category_id = request.GET.get('category', '')
    if category_id:
        books = books.filter(category_id=category_id)
    
    # Context data to send to template
    context = {
        'books': books,
        'categories': categories,
        'section': section,
        'search_query': search_query,
        'selected_category': category_id,
    }
    
    return render(request, 'book_list.html', context)

# Book detail page
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


def login_view(request):
    if request.method == 'POST':
        # Get submitted username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        print("User:", user)
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('adminLogin')  # Redirect to admin dashboard
        else:
            # Show error message
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


def contact(request):
    return render(request, 'contact.html')


@login_required
def adminLogin(request):
    return render(request, 'admin.html')


def logout_view(request):
    logout(request)
    return redirect('login')