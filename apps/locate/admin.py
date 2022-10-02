from django.contrib import admin
from .models import Category, Info, Type, Coupon
# Register your models here.

admin.site.register(Category)
admin.site.register(Info)
admin.site.register(Type)
admin.site.register(Coupon)

