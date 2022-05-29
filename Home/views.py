from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages
from django.contrib.auth import  authenticate , get_user_model , login
from django.contrib.auth.models import User
from Home.forms import UserResgistrationForm

from .models import ( 
		Portfolio,
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
 
 
