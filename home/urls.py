from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin customization

admin.site.site_header = "My Portfolio"
admin.site.site_title = "My Portfolio"
admin.site.index_title = "Welcome!In My Portfolio Portal"


urlpatterns = [
    path('home', views.home, name="home"),
]