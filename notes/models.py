from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='media/notes', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # relations between models
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    # to delete 
    # on_sale = models.BooleanField(default=False)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.IntegerField(default=0)
    def __str__(self):
        return self.title