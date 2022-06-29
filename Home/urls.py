from django.urls import path
from Home import views
from django.contrib.auth import views as auth_views

app_name = "Home"

urlpatterns = [
  path('',views.home, name='home'),
  path("register/",views.register, name='register'),
  path('login/', views.login_fn, name='login'),
  path('aboutus/',views.about_us, name='aboutus'),
  path('contactus/',views.contact_us, name='contactus'),
  path("logout/", views.logout, name='logout'),
  path("shop/", views.shop, name='shop'),
  path("ourservices/", views.services, name='ourservices'),
  path("ambulance/", views.ambulance, name='ambulance'),
  path("doctors/", views.doctors, name='doctors'),
  path("helpsection/", views.helpsection, name='helpsection'),
  path("productdetails/", views.product_details, name='productdetails'),

  path("cart/", views.cart, name='cart'),
  path("prescription/<int:p_id>/", views.prescription, name='prescription'),

   
  path('blog/',views.Blogview.as_view(), name="blog"),
  path('blog_two/<slug:slug>', views.Blogdetailview.as_view(), name="blog_two"),
  path('portfolio/',views.Portfolioview.as_view(), name="portfolio"),
  path('portfolio_two/<slug:slug>', views.Portfoliodetailview.as_view(), name="portfolio_two"),

  path("password_reset/", views.password_reset_request, name="password_reset"),

  path("dash/", views.dash, name='dash'),
  path('resetpassword/', views.resetpassword, name='resetpassword'),
  path('editprofile/', views.edit_profile ,name='editprofile'),

  path('cart', views.cart, name='cart'),
  path('addcart/<int:product_id>/', views.addcart, name="addcart"),
  path('remove/<int:product_id>/', views.remove, name='remove'),

  path("search/", views.SearchView, name="search"),
  path("searchresult/", views.searchresult, name="searchresult"),
  path("cartdash/", views.cartdash, name="cartdash"),
  path("payments/", views.payments, name="payments"),

]

