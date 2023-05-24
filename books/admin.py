from django.contrib import admin
from .models import Book, BorrowRecord


# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'register_date', 'borrower', 'is_borrowed', 'borrow_time')


class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ('book', 'borrower', 'borrow_time', 'return_time')


admin.site.register(Book, BooksAdmin)
admin.site.register(BorrowRecord, BorrowRecordAdmin)
