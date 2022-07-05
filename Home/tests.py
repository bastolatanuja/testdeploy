from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

 
# Create your tests here.

def test_case_forgotpassword_url(self):
        url=reverse('Home:password_reset')
        self.assertEquals(resolve(url).func,password_reset_request) 

def test_case_shop_url(self):
        url=reverse('Home:shop')
        self.assertEquals(resolve(url).func,shop) 


def test_case_contactus_url(self):
        url=reverse('Home:contactus')
        self.assertEquals(resolve(url).func,contact_us) 

