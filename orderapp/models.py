"""models"""
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Customer(models.Model):
    """costaomer models"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(
        upload_to="files/user_avatar", null=False, blank=False)
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return f"{self.user.username}"


class Product(models.Model):
    """product models"""
    title = models.CharField(max_length=50, null=False, blank=False)
    cover = models.FileField(
        upload_to="files/product_cover", null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class OrderApp(models.Model):
    """order models"""
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    description = RichTextField()

    def __str__(self):
        return f"{self.customer} {self.product}"
