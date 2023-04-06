# Codecs write is fine
with codecs.open('/tmp/utf8', 'w', 'utf-8') as f:
    f.write(i)

# Logging gives a Traceback
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
handler = logging.FileHandler('/tmp/out', 'w', 'utf-8')
handler.setFormatter(logging.Formatter(u'[%(levelname)s] %(message)s'))
# I've also tried nixing setFormatter and going with the default
log.addHandler(handler)
log.debug(u"process_clusters: From CSV: %s", i)
# I've also tried a bare call to i, with and without the u in the message, and explicitly i.encode('utf8'); all Tracebacks.