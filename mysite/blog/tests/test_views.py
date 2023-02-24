from django.test import TestCase, Client
# import unittest
# import os

from django.urls import reverse
# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


class ExampleTest(TestCase):
   
   @classmethod
   def setUpTestData(cls):
      cls.client = Client()
   
   def test_ex(self):
      self.assertEqual(1, 1)
      
   def test_view_list(self):
      response = self.client.get(reverse('blog:post_list'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'blog/post/list.html')



