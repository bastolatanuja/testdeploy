from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

 
# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_case_prescription_url(self):
        url=reverse('Home:prescription')
        self.assertEquals(resolve(url).func,prescription) 
    
    def test_case_cart_url(self):
        url=reverse('Home:cart')
        self.assertEquals(resolve(url).func,cart)  
        
    def test_case_addcart_url(self):
        url=reverse('Home:addcart',args=[1])
        self.assertEquals(resolve(url).func,addcart)
     

    








