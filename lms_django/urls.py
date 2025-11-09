from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # User registration URLs
    path('lessons/', include('lessons.urls')),
    path('quiz/', include('quiz.urls')),
]
