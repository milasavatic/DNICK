from django.contrib import admin
from .models import PublishingHouse, Book


# Register your models here.
class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "country", "year", "website")

    def has_add_permission(self, request):
        return True


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "pageNum", "type", "cat", "price")

    def has_add_permission(self, request):
        return True


admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Book, BookAdmin)
