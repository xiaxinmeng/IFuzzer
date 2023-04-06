
import pprint

class MyDict(dict):
    def __repr__(self):
        return 'I do my own thing'*50


if __name__ == '__main__':
    d=MyDict()
    for i in range(50):
        d['a%s'%i] = i

    pprint.pprint(d)
