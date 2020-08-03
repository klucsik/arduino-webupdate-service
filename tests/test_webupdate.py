import unittest

from myapp import app


class new_version(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()


    def test_new_version(self):
        # Given the server has a folder with binary named 'test'
        # And it has a binary with version 0_1
        # The test binary is part of the prod deploy, we don't need setup
        
        # When I make a request with name: 'test' and version: '0_0'
        params='?name=test&ver=0_0'
        response = self.app.get('/check'+params)

        # Then I get a response: '/static/bin/test/0_1.bin'
        self.assertEqual(b'/static/bin/test/0_1.bin', response.data)
        self.assertEqual(200, response.status_code)

    def test_no_new_version(self):
        # Given the server has a folder with binary named 'test'
        # And it has a binary with version 0_1
        # The test binary is part of the prod deploy, we don't need setup
        
        # When I make a request with name: 'test' and version: '0_1'
        params='?name=test&ver=0_1'
        response = self.app.get('/check'+params)

        # Then I get a response: 'update not needed'
        self.assertEqual(b'update not needed', response.data)
        self.assertEqual(200, response.status_code)

    def test_no_device_name(self):
        # Given the server doesn't have a folder with name: 'notexist'
        # The test binaries is part of the prod deploy, we don't need setup
        
        # When I make a request with name: 'notexist' and version: '0_0'
        params='?name=notexist&ver=0_0'
        response = self.app.get('/check'+params)

        # Then I get a response with status code 404
        self.assertEqual(404, response.status_code)
