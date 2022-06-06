from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

app_name = "Home"

urlpatterns = [
   path('',views.home, name='home'),
   path('editprofile/',views.editprofile, name='editprofile'),
   path("register/",views.register, name='register'),
   path('login/', views.login_fn, name='login'),
   path('home_fn/',views.home_fn, name='home_fn'),
   path('aboutus/',views.about_us, name='aboutus'),
   path('contactus/',views.contact_us, name='contactus'),
   path("logout/", views.logout, name='logout'),
   path("shop/", views.shop, name='shop'),
   
   path('blog/',views.Blogview.as_view(), name="blog"),
   path('blog_two/<slug:slug>', views.Blogdetailview.as_view(), name="blog_two"),
   path('portfolio/',views.Portfolioview.as_view(), name="portfolio"),
   path('portfolio_two/<slug:slug>', views.Portfoliodetailview.as_view(), name="portfolio_two"),

   path("password_reset/", views.password_reset_request, name="password_reset"),

  
]

