"""Complain_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from complaints.views import complaint_list
from django.contrib.auth import views as auth_views
import users.urls; print("✅ users.urls imported")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', user_views.comingSoon,name='comingSoon'),
    path('register/',user_views.register,name='register'),
    path('', complaint_list, name='complaint-list'),
    path('home/',user_views.home,name='home'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('complaints/', include('complaints.urls')),
    path('users/', include('users.urls')),


]

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)