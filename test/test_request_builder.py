from test import BaseTestClass
from src.request_builder import RequestBuilder


class TestRequestClient(BaseTestClass):

    def test_request_get_without_endpoint_and_auth(self):
        expect_method = 'GET'

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method)

        self.assertIsInstance(request_utl, dict)
        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('url', None), self.api)

    def test_request_get_with_endpoint_and_auth_bearer_query_string(self):
        expect_method = 'GET'
        expect_endpoint = '/api/v1/test'
        expect_bearer = 'f1338ca26835863f671403941738a7b49e740fc0'
        expect_query_string = {
            'type': 1,
            'order': 'asc'
            }

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method,
                                                    endpoint=expect_endpoint,
                                                    query_string=expect_query_string,
                                                    access_token=expect_bearer)

        self.assertIsInstance(request_utl, dict)
        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('url', None),
                         f'{self.api}{expect_endpoint}?type=1&order=asc')

    def test_request_get_with_endpoint_and_auth_bearer_without_param_query_string(self):
        expect_method = 'GET'
        expect_endpoint = '/api/v1/test?type=1&order=asc'
        expect_bearer = 'f1338ca26835863f671403941738a7b49e740fc0'

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method,
                                                    endpoint=expect_endpoint,
                                                    access_token=expect_bearer)

        self.assertIsInstance(request_utl, dict)
        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('url', None),
                         f'{self.api}{expect_endpoint}')

        self.assertEqual(request_utl['headers'].get('Authorization', None),
                         f'Bearer {expect_bearer}')

    def test_request_post_with_endpoint_and_without_auth(self):
        expect_method = 'POST'
        expect_endpoint = '/api/v1/test'

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method,
                                                    endpoint=expect_endpoint)

        self.assertIsInstance(request_utl, dict)
        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('url', None),
                         f'{self.api}{expect_endpoint}')

    def test_request_post_with_endpoint_and_bearer_and_body_json(self):
        expect_method = 'POST'
        expect_endpoint = '/api/v1/test'
        expect_bearer = 'f1338ca26835863f671403941738a7b49e740fc0'
        expect_body = {
            'test': 1
            }

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method,
                                                    endpoint=expect_endpoint,
                                                    access_token=expect_bearer,
                                                    json=expect_body)

        self.assertIsInstance(request_utl, dict)
        self.assertIsInstance(request_utl.get('json', None), dict)
        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('json', None), expect_body)

        self.assertEqual(request_utl.get('url', None),
                         f'{self.api}{expect_endpoint}')

        self.assertEqual(request_utl['headers'].get('Authorization', None),
                         f'Bearer {expect_bearer}')

    def test_request_put_with_endpoint_and_auth_basic(self):
        from requests.auth import HTTPBasicAuth

        expect_method = 'PUT'
        expect_endpoint = '/api/v1/test/1'

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method,
                                                    endpoint=expect_endpoint,
                                                    username='text',
                                                    password='12345678')

        self.assertIsInstance(request_utl, dict)
        self.assertIsInstance(request_utl['auth'], HTTPBasicAuth)

        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('url', None),
                         f'{self.api}{expect_endpoint}')

    def test_request_put_with_endpoint_and_bearer_and_body_form(self):
        expect_method = 'PUT'
        expect_endpoint = '/api/v1/test/1'
        expect_bearer = 'f1338ca26835863f671403941738a7b49e740fc0'
        expect_body = {
            'test': 1
            }

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method,
                                                    endpoint=expect_endpoint,
                                                    access_token=expect_bearer,
                                                    data=expect_body)

        self.assertIsInstance(request_utl, dict)
        self.assertIsInstance(request_utl.get('data', None), dict)
        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('data', None), expect_body)
        self.assertEqual(request_utl.get('url', None),
                         f'{self.api}{expect_endpoint}')

        self.assertEqual(request_utl['headers'].get('Content-Type', None),
                         'application/x-www-form-urlencoded')

        self.assertEqual(request_utl['headers'].get('Authorization', None),
                         f'Bearer {expect_bearer}')

    def test_request_delete_with_endpoint_and_auth_bearer(self):
        expect_method = 'DELETE'
        expect_endpoint = '/api/v1/test/1'
        expect_bearer = 'f1338ca26835863f671403941738a7b49e740fc0'

        builder_request = RequestBuilder(self.api)
        request_utl = builder_request.build_request(expect_method,
                                                    endpoint=expect_endpoint,
                                                    access_token=expect_bearer)

        self.assertIsInstance(request_utl, dict)
        self.assertEqual(request_utl.get('method', None), expect_method)
        self.assertEqual(request_utl.get('url', None),
                         f'{self.api}{expect_endpoint}')

        self.assertEqual(request_utl['headers'].get('Authorization', None),
                         f'Bearer {expect_bearer}')
