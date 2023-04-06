self.addCleanup(lambda: setattr(keyword, 'kwlist', oldlist))

self.addCleanup(setattr, keyword, 'kwlist', oldlist)