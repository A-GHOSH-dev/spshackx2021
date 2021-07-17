from django.contrib import admin
from django.urls import path, include
from hackxsps import views

admin.site.site_header ="Developer Ananya Ghosh"
admin.site.site_title= "Welcome to my dashboard"
admin.site.index_title="Welcome to my portal"

urlpatterns = [
    
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('submission', views.submission, name='submission'),
    path('checkin', views.checkin, name='checkin'),
    path('projects', views.projects, name='projects')

    
    
]
