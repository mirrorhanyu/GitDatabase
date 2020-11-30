import unittest


class TestClient(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')