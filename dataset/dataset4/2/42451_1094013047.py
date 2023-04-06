import logging

class X:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

def main():
    obj = X(u'\u00f6')
    logging.error(u'%s' % obj)
    logging.error(u'%s', obj)
    logging.error(u'%s-\u00f6', obj)

if __name__ == "__main__":
    main()
#