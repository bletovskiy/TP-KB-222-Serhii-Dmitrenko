from main import *
import unittest

class TestCalculator(unittest.TestCase):

    def test_isNumber(self):
        self.assertTrue(isNumber('123'))
        self.assertFalse(isNumber('+'))
        self.assertFalse(isNumber('*'))

    def test_getOper(self):
        self.assertEqual(getOper('+'), 0)
        self.assertEqual(getOper('*'), 1)
        self.assertEqual(getOper('^'), 2)

    def test_getRpn(self):
        self.assertEqual(getRpn('22 / 11 + 23 * 2 * ( 24 / 2 ) ^ 2'), ['22', '11', '/', '23', '2', '*', '24', '2', '/', '2', '^', '*', '+'])
        self.assertEqual(getRpn('48 / 4 + 156 * 24 * ( 40 / 5 ) ^ 4'), ['48', '4', '/', '156', '24', '*', '40', '5', '/', '4', '^', '*', '+'])

    def test_calcRpn(self):
        self.assertEqual(calcRpn(['22', '11', '/', '23', '2', '*', '24', '2', '/', '2', '^', '*', '+']), [6626.0])
        self.assertEqual(calcRpn(['48', '4', '/', '156', '24', '*', '40', '5', '/', '4', '^', '*', '+']), [15335436.0])

if __name__ == '__main__':
    unittest.main()