from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AboutViewTests(TestCase):
    """
    Tests for the about app views.
    """
    def setUp(self):
        # Set up any initial data or state needed for the tests
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass')

    def test_about_page_status_code(self):
        # Test that the about page returns a 200 status code
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_template_used(self):
        # Test that the about page uses the correct template
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about/about.html')

    def test_about_page_for_unauthenticated_user(self):
        # Test that the about page behaves correctly for
        # an unauthenticated user
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
        self.assertContains(response, 'About')
        self.assertContains(response, 'Sign Up')

    def test_about_page_for_authenticated_user(self):
        # Test that the about page behaves correctly for an authenticated user
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
        self.assertContains(response, 'About')
        self.assertContains(response, 'My Scrapbooks')
