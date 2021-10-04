from django.contrib import admin
from django.urls import path
from django.conf.urls import  include, url
from . import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('hello/', 'myapp.views.hello',name='hello'),
# ]

urlpatterns = [ 
    path('', views.hello, name='hello'),
    ]