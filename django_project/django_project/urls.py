"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include

from users import views as users_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Default URL:
    path(route='', view=include(arg='blog.urls')),

    # Admin URL:
    path(route='admin/', view=admin.site.urls),

    # Register URL:
    path(route='register/', view=users_views.register, name='register'),

    # Profile URL:
    path(route='profile/', view=users_views.profile, name='profile'),

    # Login and Logout URL:
    path(route='login/', view=auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path(route='logout/', view=auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

