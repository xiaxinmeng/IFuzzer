unverified_ssl_handler = urllib2.HTTPSHandler(context=ssl._create_unverified_context())
opener = urllib2.build_opener(unverified_ssl_handler)