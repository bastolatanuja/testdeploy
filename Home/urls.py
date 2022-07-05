from django.urls import path
from Home import views

app_name = "Home"

urlpatterns = [
   path('',views.home, name='home'),
   path("register/",views.register, name='register'),
   path('login/', views.login_fn, name='login'),
   path('home_fn/',views.home_fn, name='home_fn'),
   
   path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	  
	path('allportfolios/',views.allPortfolioView.as_view(),name="allportfolios"),
   path('blog/',views.blog.as_view(),name="myblog"),
   path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
]

