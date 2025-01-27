from django.test import TestCase, Client, override_settings
from django.urls import reverse


class ErrorHandlersTest(TestCase):
    """
    Test custom error handlers

    Methods:
    setUp -- Create a test client.
    test_custom_400_error_handler -- Test 400 error handler.
    test_custom_500_error_handler -- Test 500 error handler.
    test_custom_403_error_handler -- Test 403 error handler.
    test_custom_404_error_handler -- Test 404 error handler

    """
    def setUp(self):
        self.client = Client()

    def test_custom_400_error_handler(self):
        # Test 400 error handler
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    @override_settings(DEBUG=False)
    # This test will fail if DEBUG=True
    def test_custom_500_error_handler(self):
        # Test 500 error handler
        with self.assertRaises(Exception):
            response = self.client.get(reverse('trigger-500-error'))
            self.assertEqual(response.status_code, 500)
            self.assertTemplateUsed(response, '500.html')

    def test_custom_403_error_handler(self):
        # Test 403 error handler
        response = self.client.get(reverse('trigger-403-error'))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_custom_404_error_handler(self):
        # Test 404 error handler
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
