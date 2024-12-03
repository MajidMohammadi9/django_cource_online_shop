from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order,OrderItem


class OrderItemInline(admin.TabularInline):
    model=OrderItem
    fields=['order','product','quantity','price',]
    extra=1


@admin.register(Order)
class OrderAdim(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display=['user','is_paid','first_name','last_name','datetime_created',]
    inlines=[
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order','product','quantity','price',]

