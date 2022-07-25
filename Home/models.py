from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from django.urls import reverse
from numpy import product, quantile

class Product(models.Model):
    available_choice = (
        ('In Stock', 'In Stock'),
        ('Out Of Stock', 'Out Of Stock'),
    )
    name = models.CharField(max_length=40)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)      
    price = models.PositiveIntegerField()
    available = models.CharField(choices=available_choice, max_length=40)
    description=models.CharField(max_length=40)
    product_photo_1 = models.ImageField(upload_to='product_image/', blank=True)
    product_photo_2 = models.ImageField(upload_to='product_image/', blank=True)
    product_photo_3 = models.ImageField(upload_to='product_image/', blank=True)
    product_photo_4 = models.ImageField(upload_to='product_image/', blank=True)
    recently_viewed = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    medicine = models.BooleanField(default=False)
    skin = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolios'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"
    
class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    def get_absolute_url(self):
        return reverse('Home:home')

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    grandTotal = models.IntegerField(default=0,blank=False,null=False)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    def get_absolute_url(self):
        return reverse('Home:home')


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_products = models.IntegerField(default=1,blank=False,null=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.product
    def get_absolute_url(self):
        return reverse('Home:home')

class prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to="prescription")
    def get_absolute_url(self):
        return reverse('Home:home')

class cashdevlivery(models.Model):
    firstname = models.CharField(max_length=50,db_index=True)
    lastname = models.CharField(max_length=50,db_index=True)
    address = models.CharField(max_length=50,db_index=True)
    contact = models.CharField(max_length=50,db_index=True)
    def get_absolute_url(self):
        return reverse('Home:home')


class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    
    def get_absolute_url(self):
        return reverse('Home:home')


class checkoutItems(models.Model):
    checkoutId = models.AutoField(primary_key=True,unique=True,auto_created=True)
    productName = models.CharField(blank=True,max_length=50)
    quantity = models.CharField(blank=True,max_length=10)
    total = models.CharField(blank=True,max_length=10)

    def __unicode__(self):
        return self.checkoutId

class cashdevlivery(models.Model):
    firstname = models.CharField(max_length=50,db_index=True)
    lastname = models.CharField(max_length=50,db_index=True)
    address = models.CharField(max_length=50,db_index=True)
    contact = models.CharField(max_length=50,db_index=True)



