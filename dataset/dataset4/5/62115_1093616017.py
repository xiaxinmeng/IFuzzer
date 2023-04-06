with codecs.open('/tmp/test.txt', 'w', encoding='iso-8859-1') as f:
   xml = XMLGenerator(f, encoding='iso-8859-1')