from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    register_date = models.DateField()
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_borrowed = models.BooleanField(default=False)
    borrow_time = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Book.objects.get(pk=self.pk)
            if orig.is_borrowed == True and self.is_borrowed == False:
                BorrowRecord.objects.create(
                    book=self,
                    borrower=orig.borrower,
                    borrow_time=self.borrow_time,
                    return_time=timezone.now(),
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_name


class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_time = models.DateField()
    return_time = models.DateField()
