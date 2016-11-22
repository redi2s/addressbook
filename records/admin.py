from django.contrib import admin

from records.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'birthdate', 'address', 'user')
    search_fields = ('fullname',)
    list_filter = ('user',)

admin.site.register(Book, BookAdmin)


