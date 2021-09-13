from custom.utils.testutiles import TestUtiles
from modules.customers.models import Customer
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase


class CustomerModelTest(TestCase):

	
	def test_create_customer(self):
		"""
			validate create customer
			@author: javillegas (jialviga00@gmail.com)
		"""
		TestUtiles.create_customer_test('123456789')
		self.assertIs(Customer.objects.all().count() > 0, True)


	def test_get_token_by_api(self):
		"""
			validate get token by API
			@author: javillegas (jialviga00@gmail.com)
		"""
		
		TestUtiles.create_user_test()
		client = APIClient()
		
		response = client.post('/signin/', {'username': TestUtiles._USER_EMAIL, 'password': 'T3ST!!!'})
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_401_UNAUTHORIZED)
		self.assertFalse(response_data.get('authenticated', None))
		
		response = client.post('/signin/', {'username': TestUtiles._USER_USERNAME, 'password': TestUtiles._USER_PASSWORD})
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertTrue(response_data.get('authenticated', None))
		self.assertContains(response, "Token")

	def test_logout_token_by_api(self):
		"""
			logout token by api
			@author: javillegas (jialviga00@gmail.com)
		"""

		TestUtiles.create_token_test()
		client = APIClient()

		response = client.post('/logout/', {'username': TestUtiles._USER_USERNAME, 'password': TestUtiles._USER_PASSWORD})
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertTrue(response_data.get('logout', None))


	def test_create_customer_by_api(self):
		"""
			validate create customer by API
			@author: javillegas (jialviga00@gmail.com)
		"""
		
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)

		response = client.post(
			'/customers/',
			{
				'identification': '12345', 
				'name': 'TEST_CUSTOMER_NAME_API',
				'address': 'TEST_CUSTOMER_ADDRESS_API',
			}
		)
		self.assertIs(response.status_code, status.HTTP_201_CREATED)
		self.assertIs(Customer.objects.all().count() > 0, True)

	def test_list_customer_by_api(self):
		"""
			validate list customer by API
			@author: javillegas (jialviga00@gmail.com)
		"""
		
		TestUtiles.create_customer_test('111111111')
		TestUtiles.create_customer_test('222222222')
		TestUtiles.create_customer_test('333333333')
		TestUtiles.create_customer_test('444444444')
		
		token = TestUtiles.create_token_test()
		client = APIClient()
		client.credentials(HTTP_AUTHORIZATION=token)
		
		""" test first page of data """
		response = client.get('/customers/', {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/customers/")
		self.assertIsNone(response_data.get('previous', False))

		""" test next page of data """
		response = client.get(response_data.get('next'), {}, format='json')
		response_data = response.json()
		self.assertIs(response.status_code, status.HTTP_200_OK)
		self.assertIs(len(response_data.get('results', [])) > 0, True)
		self.assertContains(response, "/customers/")
		self.assertIsNone(response_data.get('next', False))
