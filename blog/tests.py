from django.test import TestCase
from django.test.client import Client
from django.utils import timezone
from blog.models import BlogPost
# Create your tests here.

class BlogPostTest(TestCase):
    csrf_Client = Client(enforce_csrf_checks=True)
    def test_obj_create(self):
        BlogPost.objects.create(title='test title', body='test body', timestamp=timezone.now())
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('test title', BlogPost.objects.get(id=1).title)

    def test_home(self):
        response = self.client.get('/blog/home')
        self.failUnlessEqual(response.status_code, 200)

    def test_archive(self):
        response = self.client.get('/blog/archive')
        self.failUnlessEqual(response.status_code, 200)

    def test_bloglist(self):
        response = self.client.get('/blog/bloglist')
        self.failUnlessEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.get('/blog/search?s=1')
        self.failUnlessEqual(response.status_code, 200)

    def test_search_redirect(self):
        response1 = self.client.get('/blog/search?s=')
        response2 = self.client.get('/blog/search')
        self.assertIn(response1.status_code, (301, 302))
        self.assertIn(response2.status_code, (301, 302))

    def test_slash(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, (301, 302))

    def test_slash2(self):
        response = self.client.get('/blog/')
        self.assertIn(response.status_code, (301, 302))

    def test_empty_create(self):
        response = self.client.get('/blog/create/')
        self.assertIn(response.status_code, (301, 302))

    def test_post_create(self):

        response = self.csrf_Client.post('/blog/create/', {'title':'post title','body':'post body'})
        self.assertIn(response.status_code, (301, 302))
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('post title',BlogPost.objects.get(id=1).title)