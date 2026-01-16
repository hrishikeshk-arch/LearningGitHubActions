"""
Tests for the API application.
"""
from django.test import TestCase, Client
from django.urls import reverse


class HealthCheckTestCase(TestCase):
    """
    Test cases for the health check endpoint.
    """
    
    def setUp(self):
        """Set up test client."""
        self.client = Client()
    
    def test_health_check_endpoint(self):
        """Test that health check endpoint returns 200 and correct data."""
        response = self.client.get(reverse('health_check'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
        
        data = response.json()
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'django-api')
    
    def test_health_check_json_structure(self):
        """Test that health check returns proper JSON structure."""
        response = self.client.get('/api/health/')
        
        self.assertIn('status', response.json())
        self.assertIn('service', response.json())

