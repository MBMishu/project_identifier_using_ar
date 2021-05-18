from django.test import TestCase, Client
from django.contrib.auth.models import User , Group
from home.model.models import Customer, Product

class TestModels(TestCase):
    
    def setUp(self):
        
        self.user2 = User.objects.create_user('mishu2','mishumishu5758@gmail.com','1234')
        
        self.customer2 = Customer.objects.create(
            user = self.user2,
            name = 'mishu2',
            phone = '01719118554',
            email = 'mishumishu5758@gmail.com'
        )
        
    
    def test_customer_model_creation(self):
        self.assertEquals(self.customer2.user.username,'mishu2')
        
    def test_product_model_creation(self):
        
        product = Product.objects.create(
            customer = self.customer2,
            name = 'new product',
        )
        self.assertEquals(product.name,'new product')
        self.assertEquals(product.customer.name,'mishu2')