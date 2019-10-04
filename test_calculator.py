import unittest
from calculator import calculate_net

class TestCalculator(unittest.TestCase):
    def test_not_number(self):
        with self.assertRaises(ValueError):
            calculate_net('10.00', 'belgium')

    def test_negative(self):
        with self.assertRaises(ValueError):
            calculate_net('-25.00', '5.00')

    def test_profit(self):
        self.assertEqual(calculate_net('10.00', '3.50')['net'], 6.50)

    def test_loss(self):
        self.assertEqual(calculate_net('300.00', '1000')['net'], -700)
