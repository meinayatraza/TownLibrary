from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Book, Category

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