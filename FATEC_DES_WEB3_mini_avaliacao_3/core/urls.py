from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('core.urls')),
]

from django.urls import path
from . import views
urlpatterns = [
path('', views.feriado),
]
