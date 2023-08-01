from django.db import models

# Create your models here.

class Book(models.Model):
    title =models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    published_date =models.DateField()
    isbn = models.CharField(max_length=13)
    amount =models.DecimalField(max_digits=10,decimal_places=2)


    def __str__(self):
        return self.title
