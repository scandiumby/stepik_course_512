#  Copyright (c) 2020, Egor N. Kostyuk, All rights reserved.
import itertools
import unittest
from .step5 import primes, primes2

class TestStep5(unittest.TestCase):

    def test_generator(self):
        result = list(itertools.takewhile(lambda x: x <= 31, primes()))
        result2 = list(itertools.takewhile(lambda x: x <= 31, primes2()))
        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
        self.assertEqual(result2, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

if __name__ == '__main__':
    unittest.main()
