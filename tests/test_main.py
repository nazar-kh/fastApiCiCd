import unittest
from fastapi.testclient import TestClient
from app.main import app


class TestFastAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(ap)

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})

    def test_say_hello(self):
        response = self.client.get("/hello/John")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello John"})


if __name__ == "__main__":
    unittest.main()
