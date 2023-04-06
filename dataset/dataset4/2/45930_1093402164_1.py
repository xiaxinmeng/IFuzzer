import time
lastyear = time.gmtime().tm_year - 1
nextyear = time.gmtime().tm_year + 1
check(_verifycert({'notAfter': 'May  9 00:00:00 %s GMT' % lastyear}, 'example.com'),
    'certificate expired May  9 00:00:00 %s GMT' % lastyear)
check(_verifycert({'notAfter': 'Sep 29 15:29:48 %s GMT' % nextyear, 'subject': ()}, 'example.com'),
    'no commonName found in certificate')
check(_verifycert(None, 'example.com'),
    'no certificate received')