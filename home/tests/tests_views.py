from django.test import TestCase, Client
from django.urls import reverse
from home.model.models import Customer, Product

import json

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.showAr = reverse('showAr')
    
    def test_showAr_Get(self):        
        response = self.client.get(self.showAr)
        
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'home/main.html')