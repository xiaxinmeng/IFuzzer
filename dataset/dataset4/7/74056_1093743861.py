import _ssl
import sys

PEM = 'Lib/test/nokia.pem'

def mem():
    with open('/proc/self/status') as f:
        for line in f:
            if line.startswith('RssAnon'):
                print(line, end='')

for i in range(10000):
    if i % 1000 == 0:
        mem()
    d = _ssl._test_decode_cert(PEM)
    assert d['crlDistributionPoints']

mem()