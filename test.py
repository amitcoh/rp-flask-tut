from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was configured correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login page is responding correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('Please Login:' in response.data)


if __name__ == "__main__":
    unittest.main()