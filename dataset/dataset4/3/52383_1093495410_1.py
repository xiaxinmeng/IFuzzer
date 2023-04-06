r = urllib.unquote(u'br%C3%BCckner_sapporo_20050930.doc')
self.assertEqual(r, u'br\xc3\xbcckner_sapporo_20050930.doc')