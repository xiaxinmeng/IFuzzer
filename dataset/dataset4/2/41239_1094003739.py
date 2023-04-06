iso = datetime.datetime.now().isoformat()
if '.' not in iso: iso = '%s.000000' % iso