from django.db import models
from ecomapp1.models import User
from django.conf import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField(null=True,blank=True)
    product_availability = models.BooleanField(default=False)
    image_url = models.URLField(max_length=2999)


    def __str__(self):
        return self.title

class Cart(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    # product = models.ForeignKey(Product,on_delete=models.CASCADE)
    # Quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart{self.id}for{self.user.username}"




class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.quantity} x {self.product.title} in cart {self.cart.id}"



