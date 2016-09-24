import unittest

from helpers.parameterized_tests import ParameterizedTest

class TestTheTruth(ParameterizedTest):
    def test_truth(self):
            self.assertTrue(True)
