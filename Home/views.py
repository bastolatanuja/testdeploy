from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages
from django.contrib.auth import  authenticate , get_user_model , login
from django.contrib.auth.models import User
from Home.forms import UserResgistrationForm
from django.views import generic
from django.shortcuts import render 
from .forms import   changeDpForm, editprofileForm
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

from .models import ( 
		Portfolio,
        Blog,
        UserProfile,
)
from django.views import generic

User = get_user_model()



def home(request):
    return render(request,'home.html')

def home_fn(request):
    return render(request,'afterlogin.html')


def register(request):
    form = UserResgistrationForm()
    if request.method =='POST':
        form = UserResgistrationForm(request.POST)
        if form.is_valid():
            print("here")
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(
                                username=username,
                                email=email,
                                first_name=first_name,
                                last_name=last_name,
                                password=password)
            user.save()
            return redirect('Home:login')
    context = {
        "form": form 
    }
    return render(request, 'registration.html')


def login_fn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect('Home:home_fn')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('Home:login')
    else:  
        return render(request, 'login.html')   










class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "portfolio-detail.html"


def allportfolio(request):
	portfolios = Portfolio.objects.all()
	return render(request,"allportfolios.html",{'portfolios':portfolios})

class allPortfolioView(generic.ListView):
	model = Portfolio
	template_name = "allportfolios.html"
	paginate_by =2
 
class blog(generic.ListView):
    model= Blog
    template_name="blog.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "Home/blog-detail.html"






def profileView(request):
	template_name="profile.html"
	return render(request,"profile.html")
 
class ChangeDP(generic.UpdateView):
	form_class = changeDpForm
	template_name = "updateImage.html"
	success_url = "/"

	def get_object(self):
		return self.request.user

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangeForm
	success_url = "/"

class editprofileView(generic.UpdateView):
	form_class = editprofileForm
	template_name = "editprofile.html"
	success_url = "/"

	def get_object(self):
		return self.request.user

class dpChangeView(generic.UpdateView):
	template_name = "updateImage.html"
	form_class = changeDpForm
	success_url = "/"
	
	def get_object(self):
		return self.request.user


def editDPView(request):
	user = request.user
	if request.method=='POST':
			newImage = request.FILES['avatar']
			obj = UserProfile.objects.get(user=user)
			obj.avatar = newImage
			obj.save()
			return render(request,'profile.html')
	else:
		return render(request, 'updateImage.html')

def SetUserImageDefault(self):
	user = self.user
	#self.user.userprofile.avatar.delete(save=True)
	return render(self,"deleteUserdp.html",{'user':user})

def delDp(request):
	if request.method=='POST':
		request.user.userprofile.avatar.delete(save=True)
		return render(request,"profile.html")
	else:
		return render(request,"deleteUserdp.html")


class allUserProfiles(generic.ListView):
	model = UserProfile
	template_name = "alluserprofile.html"
 
class updateUserProfile(generic.UpdateView):
	model = UserProfile
	template_name = "editUserProfile.html"
	fields = '__all__'
 