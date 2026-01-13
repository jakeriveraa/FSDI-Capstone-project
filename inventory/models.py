from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.stock > 0

    # CRUD methods
    @classmethod
    def create_product(cls, name, price, stock, description=""):
        product = cls(name=name, price=price, stock=stock, description=description)
        product.save()
        return product

    @classmethod
    def update_product(cls, product_id, name=None, price=None, stock=None, description=None):
        try:
            product = cls.objects.get(id=product_id)
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if stock is not None:
                product.stock = stock
            if description is not None:
                product.description = description
            product.save()
            return product
        except cls.DoesNotExist:
            return None

    @classmethod
    def delete_product(cls, product_id):
        try:
            product = cls.objects.get(id=product_id)
            product.delete()
            return True
        except cls.DoesNotExist:
            return False
