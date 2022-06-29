from tokenize import Number
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from django.urls.conf import include
from django.contrib import messages
from django.contrib.auth import  authenticate , get_user_model , login , logout
from django.contrib.auth.models import User ,auth
from Home.forms import UserResetForm, UserResgistrationForm, UserUpdateForm
from django.views import generic
from django.shortcuts import render 
from django.core.mail import send_mail, EmailMessage
from django.views import generic
from .models import Blog
from.models import Portfolio, Product
from Home.forms import UserResgistrationForm
from . import forms
from . import models
from .models import Cart, CartItem

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
    recently_viewed = models.Product.objects.filter(recently_viewed=True)
    featured = models.Product.objects.filter(featured=True)
    medicine = models.Product.objects.filter(medicine=True)
    skin = models.Product.objects.filter(skin=True)
    products=models.Product.objects.all()
    data = {
        'products':products,
        'recently_viewed': recently_viewed,
        'featured':featured,
        'medicine':medicine,
        'skin':skin,    
    }
    return render(request, 'pages/home.html', data)


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
	return render(request=request, template_name="accounts/password_reset_form.html",
        context={"password_reset_form":password_reset_form})

 

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
            [ email ], #To email
        )
        messages.success(request, "Thanks for sending the message! We'll get back to you later")
        return render(request, 'pages/contactus.html')

    else:
        return render(request,'pages/contactus.html')


def blog(request):
    return render(request,'pages/blog.html')

def portfolio(request):
    return render(request,'pages/portfolio.html')

def blog_two(request):
    return render(request,'pages/blog2.html')

def portfolio_two(request):
    return render(request,'pages/portfolio2.html')

def shop(request):
    products=models.Product.objects.all()
    data = {
        'products':products,
     
    }
    return render(request, 'shop/shop.html', data)
    

def services(request):
    return render(request,'pages/ourservices.html')

def ambulance(request):
    return render(request,'pages/ambulance.html')

def doctors(request):
    return render(request,'pages/doctors.html')

def helpsection(request):
    return render(request,'pages/helpsection.html')


def prescription(request, p_id):
    product = Product.objects.get(id=p_id)
    return render(request,'pages/prescription.html', {"product" : product})

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
    user = User.objects.get(id=request.user.id)
    print(user.password)
    if request.method == "POST":
        password = request.POST['password']
        conpassword = request.POST['confirmpassword']
        user.set_password(password)
        user.save()
        auth.logout(request)
        return redirect("/")
    return render(request,'pages/resetpassword.html')     

def edit_profile(request):
    user=User.objects.get(id=request.user.id)
    # userForm=UserResgistrationForm(instance=user)
    if request.method=='POST':
        userForm1=UserUpdateForm(request.POST, request.FILES, instance=user)
        print(userForm1)
        if userForm1.is_valid():
            print('hello')
            userForm1.save()
            messages.success(request, "Account Sucessfully Updated")
            return redirect('/dash/')
    return render(request,'pages/editprofile.html',{'user':user})

def _cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id

def addcart(request, product_id):
    current_user = request.user
    product = Product.objects.get(id=product_id)

    if request.method == "POST":

        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

        is_cart_item_exists = CartItem.objects.filter(product=product, cart=cart).exists()
        if is_cart_item_exists:
            messages.success(request, "Item Already In Cart")
            return redirect('Home:cart')
        else:
            cart_item = CartItem.objects.create(
                product=product,
                cart=cart,
                user=current_user,
            )
            cart_item.save()
            messages.success(request, "Item Added In Cart")

        return redirect('Home:cart')

def remove(request, product_id):
    product = CartItem.objects.get(id=product_id)
    product.delete()
    return redirect("Home:cart")
    
def cart(request, cart_items=None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.all().filter(user=request.user)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart, is_active=True)
    except:
        pass

    context = {
        "cart_items": cart_items,
    }

    return render(request, 'pages/cart.html', context)



def SearchView(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains =query)
    context ={ 'products':products}
    return render(request,'pages/search.html',context)    

def searchresult(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains =query)
    context ={ 'products':products}
    return render(request,'pages/search.html',context)  



def cartdash(request):
    return render(request,'pages/cartdash.html')    