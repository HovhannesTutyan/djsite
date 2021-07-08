from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cats/<slug:catslug>/', categories),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]