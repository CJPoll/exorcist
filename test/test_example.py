import unittest

from helpers.parameterized_tests import ParameterizedTest


class TestTheTruth(ParameterizedTest):
    def test_truth(self):
        self.assertTrue(self.params[0])


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParameterizedTest.parameterize(TestTheTruth, True))
    suite.addTest(ParameterizedTest.parameterize(TestTheTruth, False))
    unittest.TextTestRunner().run(suite)
