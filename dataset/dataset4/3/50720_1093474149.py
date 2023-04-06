from urllib.request import urlopen
try:
    urlopen('http://www.pythonfoobarbaz.org')
except Exception as exc:
    print('err:', err)
    print('repr(err):', repr(err))
    print('err.reason:', err.reason)
    print('repr(err.reason):', repr(err.reason))