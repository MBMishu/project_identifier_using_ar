from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.controller.views import showAr

class TesttUrls(SimpleTestCase):
    
    def test_showAr_url_is_resolved(self):
        # assert 1 == 2
        url = reverse('showAr')
        # print(resolve(url))
        self.assertEquals(resolve(url).func,showAr)
        