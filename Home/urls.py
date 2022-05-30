from django.urls import path
from Home import views

app_name = "Home"

urlpatterns = [
   path('home/',views.home, name='home'),
   path("register/",views.register, name='register'),
   path('login/', views.login_fn, name='login'),
   path('home_fn/',views.home_fn, name='home_fn'),
   
   
   
   path('', views.PortfolioView.as_view(), name="portfolio"),
   path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
	  
    
   path('blog/',views.blog.as_view(),name="myblog"),
   path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
   
   
   path('profile/',views.profileView,name="profile"),
   path('editprofile/',views.editprofileView.as_view(),name="editprofile"),
	path('changedp/',views.editDPView,name="changedp"),
	path('updateDP/',views.dpChangeView.as_view(),name="updateDP"),
	path('deletedp/',views.SetUserImageDefault,name="deletedp"),
	 
 
	path('updateUserProfile/<int:pk>',views.updateUserProfile.as_view(),name="updateUserProfile"),
 
	path('delDp/',views.delDp,name="delDp"),
]

