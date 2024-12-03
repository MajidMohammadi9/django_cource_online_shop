from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _
from products.models import Product


class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    first_name=models.CharField(verbose_name=_('First Name'),max_length=100)
    last_name=models.CharField(verbose_name=_('Last Name'),max_length=100)
    phone_number=models.CharField(verbose_name=_('Phone Number'),max_length=15)  # you can install django-phonenumber-field then use it
    address=models.CharField(verbose_name=_('Address'),max_length=700)
    order_note=models.CharField(verbose_name=_('Note'),max_length=700,blank=True)
    datetime_created=models.DateTimeField(verbose_name=_('Date Time Created'),auto_now_add=True)
    datetime_modified=models.DateTimeField(verbose_name=_('Date Time Modified'),auto_now=True)
        
    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items',verbose_name=_('Order'))
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items',verbose_name=_('Product'))
    quantity=models.PositiveIntegerField(verbose_name=_('Quantity'),default=1)
    price=models.PositiveIntegerField(verbose_name=_('Price'))

    def __str__(self):
        return f'Order Item {self.id}: {self.product} x {self.quantity}'
