expected = {
  'input1': 'output1',
  'input2': 'output2',
}

def test_encode(self):    # collapse all
    for input, output in expected.items():
        self._encode(input, output)    # test logic