import unittest
import doctest
import uzd3.perfect_number


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(uzd3.perfect_number))
    return tests


if __name__ == '__main__':
    unittest.main()
