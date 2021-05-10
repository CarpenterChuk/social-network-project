from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APITestCase
from django.db import connection
from django.urls import reverse
from django.contrib.auth import get_user_model
from posts.models import Post
from profiles.models import Profile


User = get_user_model()


# class TestListApiView(APITestCase):
#     def test_api(self):
#         pass
#

class SocialNetworkTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='testfortest', password='password')
        self.profile = Profile.objects.create(
            first_name='testfortest',
            last_name='testfortest',
            user=self.user.id,
            bio='testfortest',
            email='testfortest@gmail.com',
            country='testfortest',
        )
        self.post = Post.objects.create(content='Some content for test', author=self.profile)

    def test_add_post(self):
        post = Post.objects.create(content='Some content for test', author=self.profile.id)
        self.assertIn(post, Post.objects.all())
