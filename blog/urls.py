from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'

urlpatterns = [
    # Homepage
    path('', views.blog_home, name='home'),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog:home'), name='logout'),
    path('register/', views.register, name='register'),

    # Post Detail
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),

    # Author-only Edit/Delete
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Place edit_profile BEFORE profile/<str:username>
    path('profile/edit/', views.profile_edit_view, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
]
