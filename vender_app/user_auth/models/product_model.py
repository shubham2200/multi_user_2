from django.db import models


class Product(models.Model):
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('abandoned', 'Abandoned'), ('completed', 'Completed')])

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, related_name="carts", blank=True)
    
    
    # def total_price(self):
    #     return sum(item.product.price * item.quantity for item in self.cart_items.all())
    
    # def __str__(self):
    #     return f"Cart for {self.products}"

