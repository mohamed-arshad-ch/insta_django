from django.urls import path
from . import views

urlpatterns=[
    path("search/<name>",views.home,name="blog-home"),   #empty path for home function
]