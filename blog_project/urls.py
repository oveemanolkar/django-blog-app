from django.contrib import admin
from django.urls import path, include  # 👈 include is required to hook the blog app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # 👈 this connects your blog app to the homepage
]
