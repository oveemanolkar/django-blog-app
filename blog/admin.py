from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Category, BlogPost

# Register custom user model
@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ['username', 'email', 'is_staff']

# Register category and blog post
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
