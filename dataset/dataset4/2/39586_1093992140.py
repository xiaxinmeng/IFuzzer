from xml.sax.saxutils import XMLGenerator

g = XMLGenerator(encoding='utf8')
STREAM_NAMESPACE = 'http://etherx.jabber.org/streams'
CLIENT_NAMESPACE = 'jabber:client'
g.startDocument()
g.startPrefixMapping('stream', STREAM_NAMESPACE)
g.startPrefixMapping('client', CLIENT_NAMESPACE)
g.startElementNS( 
    (STREAM_NAMESPACE, 'stream'), 'stream',
    {(None,'xmlns'): CLIENT_NAMESPACE}
    )