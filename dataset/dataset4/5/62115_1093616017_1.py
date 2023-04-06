with codecs.open('/tmp/test.txt', 'w', encoding='utf-8') as f:
   xml = XMLGenerator(f, encoding='iso-8859-1')