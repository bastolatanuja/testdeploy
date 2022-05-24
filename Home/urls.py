from django.urls import path
from Home import views

app_name = "Home"

urlpatterns = [
   path('',views.home, name='home'),
   path("register/",views.register, name='register'),
   path('login/', views.login_fn, name='login'),
   path('home_fn/',views.home_fn, name='home_fn'),
]

