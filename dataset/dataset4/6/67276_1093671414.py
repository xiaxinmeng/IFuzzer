import unittest

class DictTest(unittest.TestCase):
    def test_dict_comprehension(self):
        code = """
d = {'a':1, 'b':2, 'c':3, 'd':4}
# global keys # UNCOMMENT FOR TEST TO PASS
keys = ['a', 'd']
items = d.items()
nd = {k: v for k, v in items if k in keys}
print('>>> ' + str(nd))
"""
        try:
            exec(code)
        except Exception as e:
            self.assertTrue(False, "Exec ERROR>>> %s" % e)

def main():
    dt = DictTest()    
    dt.test_dict_comprehension()

if  __name__ =='__main__':main()