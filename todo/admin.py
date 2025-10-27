from django.contrib import admin
from .views import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at', 'updated_at')
    search_fields = ('title',)

admin.site.register(Todo,TodoAdmin)