import pprint

class MyDict(dict):
    def __repr__(self):
        return '*'*len(dict.__repr__(self))

if __name__ == '__main__':
    d=MyDict({})
    print('pprint.pformat(d):\n%s' % pprint.pformat(d))
    print('pprint.pformat(d, width=1, indent=0):\n%s' % pprint.pformat(d, width=1, indent=0))