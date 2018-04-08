# coding: utf-8

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from polls import apiviews


class TestPoll(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'
        self.user = self.setup_user()

    @staticmethod
    def setup_user():
        user_model_class = get_user_model()
        return user_model_class.objects.create_user(
            'test',
            email='test_user@test.com',
            password='test'
        )

    def test_list_use_api_request_factory(self):
        request = self.factory.get(self.uri)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected response code 200, received {} instead'.format(
                             response.status_code))

    def test_list_use_api_client(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected response code 200, received {} instead'.format(
                             response.status_code))
