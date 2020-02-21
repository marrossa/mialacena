import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Product

def create_product(name, days):
    """Create a product with the given name and expiration
    date given the number of 'days' offset to now
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Product.objects.create(name=name, exp_date=time)

class ProductIndexJsonViewTests(TestCase):
    def test_no_products(self):
        """
        If no products exist, appropiate message is displayed
        """
        response = self.client.get(reverse('products:index_json'))
        self.assertEquals(response.status_code, 200)
        #self.assertContains(response, "No products available")
        #self.assertQuerysetEqual(response.context['products'], [])

class ProductIndexViewTests(TestCase):
    def test_no_products(self):
        """
        If no products exist, an appropiate message is displayed
        """
        response = self.client.get(reverse('products:index'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "No products available")
        self.assertQuerysetEqual(response.context['products'], [])

    def test_products_in_list(self):
        """
        If there are products, show them in the index page
        """
        create_product(name='My product', days=15)
        response = self.client.get(reverse('products:index'))
        self.assertQuerysetEqual(response.context['products'], ['<Product: My product>'])

class ProductDetailViewTests(TestCase):
    def test_product(self):
        """
        The detail view for a product
        """
        product = create_product(name='My product', days=180)
        url = reverse('products:detail', args=(product.id,))
        response = self.client.get(url)
        self.assertContains(response, product.name)
                
class ProductModelTests(TestCase):

    def test_it_is_expired(self):
        """
        expired() returns true whose products exp_date < today's date
        """
        exp_date = timezone.now().date() - datetime.timedelta(days=5)
        expired_product = Product(exp_date=exp_date)
        self.assertIs(expired_product.expired, True)

    def test_it_is_not_expired(self):
        """
        expired() returns false if the product expiration date
        has not been reach
        """
        exp_date = timezone.now().date() + datetime.timedelta(days=30)
        product = Product(exp_date=exp_date)
        self.assertIs(product.expired, False)
