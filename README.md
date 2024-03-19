# Ex02 Django ORM Web Application
## Date:29-02-2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
<img width="584" alt="image" src="https://github.com/1808charitha/ORM/assets/132996838/8b349fcd-d8fe-4f7a-bf50-f24179d87c2e">



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py
class Books(models.Model):
  Book_id=models.IntegerField(primary_key=True);
  Book_author=models.CharField(max_length=20);
  Book_name=models.CharField(max_length=50);
  publication=models.DateField();
  price=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
  list_display=("Book_id","Book_author","Book_name","publication","price");

admin.py
from django.contrib import admin
from .models import Books,BooksAdmin
admin.site.register(Books,BooksAdmin)
```


## OUTPUT
![alt text](<booklist ss.png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
