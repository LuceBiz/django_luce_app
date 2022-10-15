from django.contrib import admin
from .models import Category, Info, Type, Coupon, Film
# Register your models here.

admin.site.register(Category)
admin.site.register(Info)
admin.site.register(Type)
admin.site.register(Coupon)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'get_tags']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def get_tags(self, obj):
        return ",".join(o for o in obj.tags.names())