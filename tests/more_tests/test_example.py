import unittest

from helpers.parameterized_tests import ParameterizedTest


class TestTheTruth(ParameterizedTest):
    def test_truth(self):
        if self.params["truth"] == True:
            self.assertTrue(self.params["truth"])
        else:
            self.assertFalse(self.params["truth"])

class MyClass():
    def __init__(self):
        self.x = 0

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParameterizedTest.parameterize(TestTheTruth, {"truth" : True}))
    suite.addTest(ParameterizedTest.parameterize(TestTheTruth, {"truth" : False}))
    unittest.TextTestRunner().run(suite)
