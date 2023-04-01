from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('main', views.index),
    path('admin/', admin.site.urls),
    path('straight', views.straight),
    path('triangle', views.triangle),
    path('quadrilateral', views.quadrilateral),
    path('area', views.area),
    path('circle', views.circle),
    path('trigonometry', views.trigonometry),
]
