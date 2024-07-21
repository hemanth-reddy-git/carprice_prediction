from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    #calling api using the js
    path('api/carprice/', views.carprice, name='carprice')
    
]