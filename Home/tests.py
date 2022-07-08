from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

 
# Create your tests here.

class TestUrls(SimpleTestCase):

<<<<<<< HEAD
    def test_case_payments_url(self):
        url=reverse('Home:payments')
        self.assertEquals(resolve(url).func,payments)
=======
    def test_case_logout_url(self):
        url=reverse('Home:logout')
        self.assertEquals(resolve(url).func,logout)      
    
    def test_case_shop_url(self):
        url=reverse('Home:shop')
        self.assertEquals(resolve(url).func,shop) 


    def test_case_password_reset_url(self):
        url=reverse('Home:password_reset')
        self.assertEquals(resolve(url).func,password_reset_request)
    
    def test_case_cashdelivery_url(self):
        url=reverse('Home:cashdelivery')
        self.assertEquals(resolve(url).func,cashdelivery)    


   
   

 

>>>>>>> e7bf551d183c050600ec9dcc8286f09bda897751









