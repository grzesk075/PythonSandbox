import unittest
import basics.static as static

class TestStatics(unittest.TestCase):

    def test_repr(self):
        name = 'test name ąśż'
        s = static.Statics(name)
        self.assertEqual(name, str(s), '__repr__ should return _name')

    def test_sum(self):
        self.assertEqual(5, static.Statics.sum(2, 3), 'sum of 2 and 3 should be 5')
        self.assertEqual('ab', static.Statics.sum('a', 'b'), 'sum of a and b should be ab')
        self.assertEqual(-2.75, static.Statics.sum(-1.5, -1.25), 'sum of -1.5 and -1.25 should be -2.75')
