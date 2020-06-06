from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ConfigurationTestCase(TestCase):
    fixtures = []

    def setUp(self):
        self.client = APIClient()

    def test_all_fields(self):
        response = self.client.get('/api/sample_api/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.json(), dict(sample_data=123))
