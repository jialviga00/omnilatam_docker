from rest_framework.authtoken.models import Token
from modules.orders.models import Order, OrderDetail
from modules.customers.models import Customer
from django.contrib.auth.models import User
from modules.products.models import Product

class TestUtiles:

	_USER_USERNAME = 'test'
	_USER_EMAIL = 'test@test.com'
	_USER_PASSWORD = 'T3ST!'

	@staticmethod
	def create_customer_test(identification, name="TEST_CUSTOMER_NAME", address="TEST_CUSTOMER_ADDRESS"):
		customer = Customer()
		customer.identification = identification
		customer.name = name
		customer.address = address
		customer.save()
		return customer

	@staticmethod
	def create_order_test():
		order = Order()
		customer = TestUtiles.create_customer_test('123456789')
		order.customer = customer
		order.save()
		return order

	def create_order_test_with_detail(extra=1):
		order = TestUtiles.create_order_test()
		product = TestUtiles.create_product_test()
		for i in range(0, extra):
			order_detail = OrderDetail()
			order_detail.order = order
			order_detail.product = product
			order_detail.amount = (i+1) * 5000
			order_detail.cant = (i+1) * 1
			order_detail.save()
		return order


	@staticmethod
	def create_product_test(name="PRODUCT_TEST_NAME", category="PRODUCT_TEST_CATEGORY", description="PRODUCT_TEST_DESCRIPTION"):
		product = Product()
		product.name = name
		product.category = category
		product.description = description
		product.save()
		return product

	@staticmethod
	def create_user_test():
		user = User.objects.create_user(TestUtiles._USER_USERNAME, TestUtiles._USER_EMAIL, TestUtiles._USER_PASSWORD)
		user.save()
		return user

	@staticmethod
	def create_token_test(user=None):
		if not user:
			user = TestUtiles.create_user_test()
		token, _ = Token.objects.get_or_create(user=user)
		return "Token " + token.key
