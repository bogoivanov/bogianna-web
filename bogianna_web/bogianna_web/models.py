from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(max_length=255, blank=True, null=True)  
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='books/')
    pdf_link = models.FileField(upload_to='books-PDF/')
    date_added = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the book is added

    def __str__(self):
        return self.title