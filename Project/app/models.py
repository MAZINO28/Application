from django.db import models
from django.urls import reverse

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

class Order (models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem (models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="items")
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="order_items")
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="products")
    categorey_id = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="primary_products")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name="alternate_products", blank=True)
    order = models.ManyToManyField(Order, related_name="products", blank=True)
    orderitem = models.ManyToManyField(OrderItem, related_name="products", blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})
