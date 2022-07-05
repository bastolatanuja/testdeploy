from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_case_logout_url(self):
        url=reverse('Home:logout')
        self.assertEquals(resolve(url).func,logout)      
    
    def test_case_portfolio_url(self):
        url=reverse('Home:portfolio')
        self.assertEquals(resolve(url).func,PortfolioView) 
