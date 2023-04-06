
sms.buf[0:6] = b'pickle'
pickled_sms = pickle.dumps(sms)
sms2 = pickle.loads(pickled_sms)
self.assertEqual(sms.name, sms2.name)
self.assertEqual(bytes(sms.buf[0:6]), bytes(sms2.buf[0:6]), b'pickle')
