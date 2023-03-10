from django.test import TestCase, Client
from django.urls import reverse

class PostListViewTest(TestCase):
   @classmethod
   def setUpTestData(cls):
      cls.client = Client()
      
   def test_view_list(self):
      response = self.client.get(reverse('blog:post_list'))
      self.assertEqual(response.status_code, 200)
      self.assertTemplateUsed(response, 'blog/post/list.html')



