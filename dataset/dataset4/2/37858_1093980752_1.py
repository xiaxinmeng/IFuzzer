class w1u(mixin):
    v1 = u'v1'

class w2u(mixin):
    def v2(self):
        return '%(v1)s' % w1u()

class w3u(mixin):
    def v3(self):
        return '%(v2)s' % w2u()

class w1(mixin):
    v1 = 'v1'

class w2(mixin):
    def v2(self):
        return '%(v1)s' % w1()

class w3(mixin):
    def v3(self):
        return '%(v2)s' % w2()