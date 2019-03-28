import unittest


class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'b'
        self.assertEqual(a, b)
