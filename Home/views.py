from tokenize import Number
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages
from django.contrib.auth import  authenticate , get_user_model , login , logout
from django.contrib.auth.models import User ,auth
from Home.forms import UserResgistrationForm
from django.views import generic
from django.shortcuts import render 
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.core.mail import send_mail
from django.views import generic
from .models import Blog
from.models import Portfolio


# For reset password
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


from django.views import generic

User = get_user_model()


def home(request):
    return render(request,'pages/home.html')

def home_fn(request):
    return render(request,'pages/afterlogin.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('Home:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('Home:register')
                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, email=email, username=username, password=password)
                    auth.login(request, user)
                    user.save()
                    messages.success(
                        request, 'You are registered successfully')
                    return redirect('Home:login')

        else:
            messages.error(request, 'Password do not match')
            return redirect('Home:register')
    else:
        return render(request, 'pages/registration.html')


def login_fn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(request.user.username)
            return redirect('Home:home')
        
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('Home:login')
    else:  
        return render(request, 'pages/login.html')   

def logout(request):
    auth.logout(request)
    return redirect('Home:home')

def about_us(request):
    return render(request, 'pages/aboutus.html') 

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'biruwahamro@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password_reset_form.html", context={"password_reset_form":password_reset_form})

 

def contact_us(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message =request.POST['message']
        number = request.POST['number']
        send_mail(
        
            name, #subject
            message, #message
            email, #from email
            ['biruwahamro@gmail.com' ], #To email
        )
        messages.success(request, "Thanks for sending the message! We'll get back to you later")
        return render(request, 'pages/contactus.html')

    else:
        return render(request,'pages/contactus.html')


def blog(request):
    return render(request,'pages/blog.html')

def editprofile(request):
    return render(request,'pages/editprofile.html')

def portfolio(request):
    return render(request,'pages/portfolio.html')

def blog_two(request):
    return render(request,'pages/blog2.html')

def portfolio_two(request):
    return render(request,'pages/portfolio2.html')

def shop(request):
    return render(request,'shop/shop.html')

class Blogview(generic.ListView):
    model=Blog
    template_name='pages/blog.html'
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Portfolioview(generic.ListView):
    model=Portfolio
    template_name='pages/portfolio.html'
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Blogdetailview(generic.DetailView):
    model=Blog
    template_name='pages/blog2.html'

class Portfoliodetailview(generic.DetailView):
    model=Portfolio
    template_name='pages/portfolio2.html'
    
def dash(request):
    return render(request,'pages/dash.html') 

def resetpassword(request):
    return render(request,'pages/resetpassword.html')      