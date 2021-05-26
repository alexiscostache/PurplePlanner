from django.urls import path
from .views import profile_home,get_data,upload_image
urlpatterns = [
    path('', profile_home, name="profile_home"),
    path('get_data/', get_data, name="get_data"),
    path('upload_image/', upload_image, name="upload_image"),


]
