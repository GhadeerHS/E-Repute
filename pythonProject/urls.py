"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include
from users import views as user_views
from dashboard import views as dashboard_views
from django.contrib.auth import views as auth_views 
# from global_login_required import login_not_required

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/', user_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('dashboard/', dashboard_views.dashboard ,name='dashboard'),
    path('check/', dashboard_views.check ,name='check'),
    path('records/', dashboard_views.records ,name='records'),
    path('edit_profile/', dashboard_views.edit_profile ,name='edit_profile'),
    # path('edit_user_profile/', dashboard_views.edit_user_profile ,name='edit_user_profile'),
    path('userslist/', dashboard_views.userslist ,name='userslist'),
    path('deleterecord/<int:id>/', dashboard_views.deleterecord, name='deleterecord'),
    path('deleteuser/<int:id>/', dashboard_views.deleteuser, name='deleteuser'),
    
    path('result/', dashboard_views.result),
    path('one_email/', dashboard_views.one_email,name='one_email'),
    path('excel_email/', dashboard_views.excel_email),

    ]


