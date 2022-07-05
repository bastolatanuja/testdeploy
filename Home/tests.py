from django import views
from django.urls import reverse,resolve
from django.test import   SimpleTestCase 
from Home.views import * 

 
# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_case_search_url(self):
        url=reverse('Home:search')
        self.assertEquals(resolve(url).func,SearchView)

    def test_case_searchresult_url(self):
        url=reverse('Home:searchresult')
        self.assertEquals(resolve(url).func,searchresult)










