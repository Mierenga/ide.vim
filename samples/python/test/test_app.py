import unittest

import app

class TestApp(unittest.TestCase):

    def setUp(self):
        pass

    def test_main_exits_with_zero(self):
        result = app.main()
        self.assertEqual(result, 0)

