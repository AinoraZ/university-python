import unittest
from rationalNumber import RationalNumber


class TestPerfectNumber(unittest.TestCase):
    def assert_rational_number(self, rationalToTest, resultNominator, resultDenominator):
        self.assertEqual(rationalToTest.numerator, resultNominator)
        self.assertEqual(rationalToTest.denominator, resultDenominator)

    def test_rational_number_add_same_denominator(self):
        self.assert_rational_number(RationalNumber(1, 2).add(RationalNumber(1, 2)), 2, 2)
        self.assert_rational_number(RationalNumber(1, 33).add(RationalNumber(5, 33)), 6, 33)
        self.assert_rational_number(RationalNumber(1, 100).add(RationalNumber(1, 100)), 2, 100)
        self.assert_rational_number(RationalNumber(1, 100).add(RationalNumber(50, 100)), 51, 100)
        self.assert_rational_number(RationalNumber(1, 100).add(RationalNumber(100, 100)), 101, 100)

    def test_rational_number_add_different_denominator(self):
        self.assert_rational_number(RationalNumber(1, 2).add(RationalNumber(1, 3)), 5, 6)
        self.assert_rational_number(RationalNumber(1, 2).add(RationalNumber(1, 4)), 6, 8)
        self.assert_rational_number(RationalNumber(1, 2).add(RationalNumber(1, 5)), 7, 10)
        self.assert_rational_number(RationalNumber(1, 3).add(RationalNumber(1, 9)), 12, 27)


if __name__ == '__main__':
    unittest.main()
