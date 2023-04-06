tmp = namedtuple('NTColor', 'red green blue')
globals().pop('NTColor', None)          # remove artifacts from other tests
self.assertNotIn('NTColor', globals())