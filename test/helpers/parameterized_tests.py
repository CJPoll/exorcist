import unittest

class ParameterizedTest(unittest.TestCase):
    def __init__(self, methodName='runTest', params=None):
        super(ParameterizedTest, self).__init__(methodName)
        self.params = params

    @staticmethod
    def parameterize(testcase, params=None):
        test_loader = unittest.TestLoader()
        test_names = test_loader.getTestCaseNames(testcase)
        suite = unittest.TestSuite()
        for name in test_names:
            suite.addTest(testcase(name, params))
        return suite
