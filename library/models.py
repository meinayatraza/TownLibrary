from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name


# Book Model
class Book(models.Model):
    SECTION_CHOICES = [
        ('male', 'Male Section'),
        ('female', 'Female Section'),
    ]
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    publisher = models.CharField(max_length=200, blank=True)
    published_year = models.IntegerField()
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    
    # Section field - Male or Female
    section = models.CharField(max_length=10, choices=SECTION_CHOICES)
    
    # Availability tracking
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    
    # Extra info
    shelf_location = models.CharField(max_length=50, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def is_available(self):
        return self.available_copies > 0
    
    class Meta:
        ordering = ['-added_date']