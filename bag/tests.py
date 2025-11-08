from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from decimal import Decimal
from datetime import date, timedelta
from products.models import Product, Category
from checkout.models import DiscountCode
from bag.contexts import bag_contents


class BagContextsTestCase(TestCase):
    """
    Test cases for bag context processor, specifically discount code logic.
    """

    def setUp(self):
        """Set up test data."""
        self.factory = RequestFactory()
        
        self.category = Category.objects.create(
            name='test_category',
            friendly_name='Test Category'
        )
        
        self.product1 = Product.objects.create(
            name='Test Product 1',
            description='Test description',
            price=Decimal('50.00'),
            category=self.category,
            sku='000001'
        )
        
        self.product2 = Product.objects.create(
            name='Test Product 2',
            description='Test description',
            price=Decimal('30.00'),
            category=self.category,
            sku='000002'
        )
        
        self.discount_code = DiscountCode.objects.create(
            code='TEST10',
            discount_type='percentage',
            discount_amount=Decimal('10.00'),
            expiration_date=date.today() + timedelta(days=30)
        )

    def _create_request_with_session(self, bag_data=None, discount_code_id=None):
        """Helper method to create a request with session data."""
        request = self.factory.get('/')
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        request.session.save()
        
        if bag_data:
            request.session['bag'] = bag_data
        if discount_code_id:
            request.session['discount_code_id'] = discount_code_id
            
        return request

    def test_bag_contents_without_discount(self):
        """Test bag contents calculation without discount code."""
        bag_data = {str(self.product1.id): 2}
        request = self._create_request_with_session(bag_data=bag_data)
        
        context = bag_contents(request)
        
        self.assertEqual(context['total'], Decimal('100.00'))
        self.assertEqual(context['discount_amount'], 0)
        self.assertEqual(context['product_count'], 2)

    def test_bag_contents_with_percentage_discount(self):
        """Test bag contents calculation with percentage discount code."""
        bag_data = {str(self.product1.id): 2}
        request = self._create_request_with_session(
            bag_data=bag_data,
            discount_code_id=self.discount_code.id
        )
        
        context = bag_contents(request)
        
        expected_subtotal = Decimal('100.00')
        expected_discount = Decimal('10.00')
        expected_total = expected_subtotal - expected_discount
        
        self.assertEqual(context['discount_amount'], expected_discount)
        self.assertEqual(context['total'], expected_total)

    def test_bag_contents_with_invalid_discount_code(self):
        """Test bag contents with non-existent discount code ID."""
        bag_data = {str(self.product1.id): 1}
        request = self._create_request_with_session(
            bag_data=bag_data,
            discount_code_id=99999
        )
        
        context = bag_contents(request)
        
        self.assertEqual(context['discount_amount'], 0)
        self.assertEqual(context['total'], Decimal('50.00'))

    def test_bag_contents_with_promotion_price(self):
        """Test bag contents with product on promotion."""
        self.product1.is_on_promotion = True
        self.product1.promotion_price = Decimal('40.00')
        self.product1.save()
        
        bag_data = {str(self.product1.id): 1}
        request = self._create_request_with_session(bag_data=bag_data)
        
        context = bag_contents(request)
        
        self.assertEqual(context['total'], Decimal('40.00'))

    def test_bag_contents_discount_on_promotion_price(self):
        """Test discount applied to promotion price."""
        self.product1.is_on_promotion = True
        self.product1.promotion_price = Decimal('40.00')
        self.product1.save()
        
        bag_data = {str(self.product1.id): 1}
        request = self._create_request_with_session(
            bag_data=bag_data,
            discount_code_id=self.discount_code.id
        )
        
        context = bag_contents(request)
        
        expected_discount = Decimal('4.00')
        expected_total = Decimal('36.00')
        
        self.assertEqual(context['discount_amount'], expected_discount)
        self.assertEqual(context['total'], expected_total)

    def test_bag_contents_multiple_products_with_discount(self):
        """Test discount calculation with multiple products."""
        bag_data = {
            str(self.product1.id): 2,
            str(self.product2.id): 1
        }
        request = self._create_request_with_session(
            bag_data=bag_data,
            discount_code_id=self.discount_code.id
        )
        
        context = bag_contents(request)
        
        expected_subtotal = Decimal('130.00')
        expected_discount = Decimal('13.00')
        expected_total = expected_subtotal - expected_discount
        
        self.assertEqual(context['discount_amount'], expected_discount)
        self.assertEqual(context['total'], expected_total)
        self.assertEqual(context['product_count'], 3)

    def test_discount_cannot_exceed_total(self):
        """Test that discount amount cannot exceed total."""
        large_discount = DiscountCode.objects.create(
            code='LARGE50',
            discount_type='percentage',
            discount_amount=Decimal('50.00'),
            expiration_date=date.today() + timedelta(days=30)
        )
        
        bag_data = {str(self.product1.id): 1}
        request = self._create_request_with_session(
            bag_data=bag_data,
            discount_code_id=large_discount.id
        )
        
        context = bag_contents(request)
        
        expected_discount = Decimal('25.00')
        expected_total = Decimal('25.00')
        
        self.assertEqual(context['discount_amount'], expected_discount)
        self.assertEqual(context['total'], expected_total)
