import uuid
from django.urls import reverse
from django.db import models


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="Title", max_length=200)
    author = models.CharField(verbose_name="Author", max_length=200)
    price = models.DecimalField(verbose_name="Price", max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id),])