from django.test import TestCase,RequestFactory
from django.test.client import Client
from django.utils import timezone
from django.contrib.auth.models import User

from blog.models import BlogPost

# Create your tests here.

class BlogPostTest(TestCase):
    csrf_Client = Client(enforce_csrf_checks=True)
    factory = RequestFactory()

    #model object
    def test_obj_create(self):
        BlogPost.objects.create(title='test title', body='test body', timestamp=timezone.now())
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('test title', BlogPost.objects.get(id=1).title)

    #archive page

    def test_archive(self):
        response = self.client.get('/blog/archive/')
        self.failUnlessEqual(response.status_code, 200)

    def test_bloglist(self):
        response = self.client.get('/blog/bloglist/')
        self.failUnlessEqual(response.status_code, 200)

    def test_search(self):
        response = self.client.get('/blog/search?s=1')
        self.failUnlessEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login/')
        self.failUnlessEqual(response.status_code, 200)

    #redirect
    def test_search_redirect(self):
        response = self.client.get('/blog/search')
        self.assertIn(response.status_code, (301, 302))
        self.assertRedirects(response, '/blog/archive/')

    def test_search_empty(self):
        response = self.client.get('/blog/search?s=')
        self.assertIn(response.status_code, (301, 302))
        self.assertRedirects(response, '/blog/archive/')

    def test_rehomo(self):
        response = self.client.get('/')
        self.assertIn(response.status_code, (301, 302))
        self.assertRedirects(response, '/home/')

    def test_reblogarchive(self):
        response = self.client.get('/blog/')
        self.assertIn(response.status_code, (301, 302))
        self.assertRedirects(response, '/blog/archive/')

    def test_login_in(self):
        User.objects.create_user('test', password='testpassword')
        response = self.csrf_Client.post('/login/in/', {'username':'test','password':'testpassword'})
        self.assertIn(response.status_code, (301, 302))
        self.assertRedirects(response, '/home/')
        response2 = self.csrf_Client.get('/home/')
        self.assertEqual('test',response2.context['user'].username)

    def test_logout(self):
        User.objects.create_user('test',password='testpassword')
        self.client.login(username='test',password='testpassword')
        response0 = self.client.get('/home/')
        self.assertEqual('test', response0.context['user'].username)
        response = self.client.get('/logout/')
        self.assertIn(response.status_code, (301, 302))
        response2 = self.client.get('/home/')
        self.assertEqual('', response2.context['user'].username)

    def test_nolog_create(self):
        response = self.client.get('/blog/create/')
        self.assertIn(response.status_code, (301, 302))
        self.assertRedirects(response,'/login/?next=/blog/create/')

    def test_login_create(self):
        User.objects.create_user('test',password='testpassword')
        self.csrf_Client.login(username='test',password='testpassword')
        response = self.csrf_Client.post('/blog/create/commit/', {'title':'post title','body':'post body'})
        self.assertIn(response.status_code, (301, 302))
        self.assertEqual(1, BlogPost.objects.count())
        self.assertEqual('post title',BlogPost.objects.get(id=1).title)
        response2 = self.client.get('/blog/archive/1/')
        self.assertEqual(response2.status_code,200)