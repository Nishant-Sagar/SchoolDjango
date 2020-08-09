from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact-us.html', views.contact, name = 'contact-us'),
    path('gallery-photo.html', views.gallery, name = 'gallery-photo'),
    path('admission.html', views.admission, name = 'admission'),
    path('about.html', views.about, name = 'about'),

]