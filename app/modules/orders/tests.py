from custom.utils.testutiles import TestUtiles
from modules.orders.models import Order, OrderDetail
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase


class OrderModelTest(TestCase):

	def test_create_order(self):
		"""
			validate create order
			@author: javillegas (jialviga00@gmail.com)
		"""
		TestUtiles.create_order_test()
		self.assertIs(Order.objects.all().count() > 0, True)
	

	def test_create_order_by_api(self):
		"""
			validate create order by API
			@author: javillegas (jialviga00@gmail.com)
		"""
		customer = TestUtiles.create_customer_test('123456789')
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)

		response = client.post(
			'/orders/',
			{
				'customer': customer.id,
			}
		)
		self.assertIs(response.status_code, status.HTTP_201_CREATED)
		self.assertIs(Order.objects.all().count() > 0, True)
		

	def test_list_order_by_api(self):
		"""
			validate list order by API
			@author: javillegas (jialviga00@gmail.com)
		"""
		
		TestUtiles.create_order_test()
		TestUtiles.create_order_test()
		TestUtiles.create_order_test()
		
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)
		
		""" test first page of data """
		response = client.get('/orders/', {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/orders/")
		self.assertIsNone(response_data.get('previous', False))

		""" test next page of data """
		response = client.get(response_data.get('next'), {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/orders/")
		self.assertIsNone(response_data.get('next', False))

	def test_add_product_by_api(self):
		"""
			validate add product to order by api
			@author: javillegas (jialviga00@gmail.com)
		"""

		order = TestUtiles.create_order_test()
		product = TestUtiles.create_product_test()
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)

		response = client.post(
			'/orders/{order_id}/add_product/'.format(order_id=order.id),
			{
				"product": product.id,
				"amount": 5000,
				"cant": 1,
			}, 
			format='json'
		)

		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(OrderDetail.objects.all().count() > 0, True)

	def test_detail_order_by_api(self):
		"""
			validate detail order by api
			@author: javillegas (jialviga00@gmail.com)
		"""

		order = TestUtiles.create_order_test_with_detail(3)
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)

		""" test first page of data """
		response = client.get('/orders/{order_id}/detail_order/'.format(order_id=order.id), {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/orders/")
		self.assertIsNone(response_data.get('previous', False))

		""" test next page of data """
		response = client.get(response_data.get('next'), {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/orders/")
		self.assertIsNone(response_data.get('next', False))
