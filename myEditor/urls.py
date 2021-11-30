"""myEditor URL Configuration

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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from photoeditor import views as photoeditor_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', photoeditor_views.photoeditor, name='photoeditor'),
    path('photoeditor_complete/', photoeditor_views.photoeditor_complete, name='photoeditor_complete'),
    # path('photoeditor_reset/', photoeditor_views.photoeditor_reset, name='photoeditor_reset'),

    # path('increase_brightness/', photoeditor_views.increase_brightness, name='increase_brightness'),
    # path('decrease_brightness/', photoeditor_views.decrease_brightness, name='decrease_brightness'),

    # path('increase_contrast/', photoeditor_views.increase_contrast, name='increase_contrast'),
    # path('decrease_contrast/', photoeditor_views.decrease_contrast, name='decrease_contrast'),

    # path('increase_sharpness/', photoeditor_views.increase_sharpness, name='increase_sharpness'),
    # path('decrease_sharpness/', photoeditor_views.decrease_sharpness, name='decrease_sharpness'),

]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    