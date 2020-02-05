# Use include() to add paths from the catalog application
from django.urls import path
from . import views
# from auto_dnup import views

urlpatterns = [
    path('', views.post_list, name='post_list')
]
