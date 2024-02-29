from django.db import models
from django.contrib import admin
class Book(models.Model):
  Book_id=models.IntegerField(primary_key=True);
  Book_author=models.CharField(max_length=20);
  Book_name=models.CharField(max_length=50);
  publication=models.DateField();
  price=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
  list_display=("Book_id","Book_author","Book_name","publication","price");
