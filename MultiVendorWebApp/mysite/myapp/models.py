from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=120)
    price=models.FloatField()
    file=models.FileField(upload_to='uploads')
    total_sales_amount=models.IntegerField(default=0)
    total_sales=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class OrderDetail(models.Model):
    customer_email=models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Product link
    instamojo_payment_request_id = models.CharField(max_length=100, blank=True)
    instamojo_payment_id = models.CharField(max_length=100, blank=True)
    amount = models.FloatField()  # Paise me bhi store kar sakte ho ya rupees me
    currency = models.CharField(max_length=10, default="INR")
    payment_status = models.CharField(max_length=20, default="created")  # created, paid, failed0
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.razorpay_order_id} for {self.product.name}"



