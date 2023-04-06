class MyAssertions:
    def assertComplexState(self, inputs):
        self.assertEqual('42', inputs[0], 'the input %s is not the right answer' % inputs)

__unittests = {'MyAssertions.assertComplexState'}