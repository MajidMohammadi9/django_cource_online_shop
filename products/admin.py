from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment


# to dispaly 'comments' in products page in admin
# Tabular inline & StackedInline
class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active']
    extra = 0  # won't show the empty box for 'comments' in admin
    # extra=1 will show only one empty box


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active']
