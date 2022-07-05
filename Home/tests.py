from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

 
# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_case_home_url(self):
        url=reverse('Home:home')
        self.assertEquals(resolve(url).func,home)

    def test_case_register_url(self):
        url=reverse('Home:register')
        self.assertEquals(resolve(url).func,register)    

    def test_case_login_url(self):
        url=reverse('Home:login')
        self.assertEquals(resolve(url).func,login_fn)    