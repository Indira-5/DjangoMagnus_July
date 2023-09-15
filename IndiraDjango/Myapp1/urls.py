from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('help/',views.help,name='help'),
    path('contact',views.contact,name='contact')

]
