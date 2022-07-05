from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

 
# Create your tests here.


def test_case_services_url(self):
    url=reverse('Home:services')
    self.assertEquals(resolve(url).func,services)

def test_case_ambulance_url(self):
    url=reverse('Home:ambulance')
    self.assertEquals(resolve(url).func,ambulance) 

def test_case_doctors_url(self):
    url=reverse('Home:doctors')
    self.assertEquals(resolve(url).func,doctors)  

def test_case_helpsection_url(self):
    url=reverse('Home:helpsection')
    self.assertEquals(resolve(url).func,helpsection)   

  