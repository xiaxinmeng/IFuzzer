import unittest

class Test(unittest.TestCase):
    def test_1(self):
        print('test_1')

    def test_2(self):
        print('test_2')
        self.fail('msg')
    
class Result(unittest.TestResult):
    def startTestRun(self, test):
        print('starttestrun', test)

    def stopTestRun(self, test):
        print('stoptestrun', test)

    def startTest(self, test):
        print('starttest', test)

    def stopTest(self, test):
        print('stoptest', test)

result = Result()
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
suite.run(result)

print(result)