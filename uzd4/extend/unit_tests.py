import unittest
from perfectNumber import perfectNumber as is_perfect_number, error


class TestPerfectNumber(unittest.TestCase):
    def test_when_string_should_raise(self):
        self.assertRaises(error, is_perfect_number, "")
        self.assertRaises(error, is_perfect_number, "Hi")
        self.assertRaises(error, is_perfect_number, "Hello")

    def test_when_array_should_raise(self):
        self.assertRaises(error, is_perfect_number, [])
        self.assertRaises(error, is_perfect_number, ["h", "i"])
        self.assertRaises(error, is_perfect_number, [1, 2, 3])
        self.assertRaises(error, is_perfect_number, [0.1])

    def test_when_float_should_be_raise(self):
        self.assertRaises(error, is_perfect_number, 0.001)
        self.assertRaises(error, is_perfect_number, 3.34)
        self.assertRaises(error, is_perfect_number, 6.000001)
        self.assertRaises(error, is_perfect_number, 0.1)
        self.assertRaises(error, is_perfect_number, -0.01)
        self.assertRaises(error, is_perfect_number, -3.1)
        self.assertRaises(error, is_perfect_number, -28.1)
        self.assertRaises(error, is_perfect_number, 6.0)
        self.assertRaises(error, is_perfect_number, 28.0)
        self.assertRaises(error, is_perfect_number, 496.0)
        self.assertRaises(error, is_perfect_number, 8128.0)
        self.assertRaises(error, is_perfect_number, 33550336.0)

    def test_when_non_perfect_int_should_be_false(self):
        self.assertFalse(is_perfect_number(0))
        self.assertFalse(is_perfect_number(1))
        self.assertFalse(is_perfect_number(2))
        self.assertFalse(is_perfect_number(3))
        self.assertFalse(is_perfect_number(14))
        self.assertFalse(is_perfect_number(33))
        self.assertFalse(is_perfect_number(188))
        self.assertFalse(is_perfect_number(-1))
        self.assertFalse(is_perfect_number(-4))
        self.assertFalse(is_perfect_number(-6))
        self.assertFalse(is_perfect_number(-28))
        self.assertFalse(is_perfect_number(-33))
        self.assertFalse(is_perfect_number(-496))

    def test_when_perfect_int_should_be_true(self):
        self.assertTrue(is_perfect_number(6))
        self.assertTrue(is_perfect_number(28))
        self.assertTrue(is_perfect_number(496))
        self.assertTrue(is_perfect_number(8128))
        self.assertTrue(is_perfect_number(33550336))


if __name__ == '__main__':
    unittest.main()
