"""formation1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls import path, include
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', include('myapp_formation.urls')), 
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'), 
        #this to confirm that email sent and check it inbox
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),    
    path('password-reset-confirm/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),    
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_confirm'),                  
       ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if we are in debug mode , chan3mlo amr heka hedha wa9t eli n7ebo taswira tbenelna fl profile kyyf nod5lo lel url te3o
if settings.DEBUG:
#here media url and media root added to the url parent ,should now make our media with the browser
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #after that use django signals bech nwaliw nasn3o profile te3na wa7adna men8ir manemchiw lel page admin 
    
