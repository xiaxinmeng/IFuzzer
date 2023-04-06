class Foo_emptydict(object):
    def __contains__(self,item): return {}

class Foo_emptystring(object):
    def __contains__(self,item): return ''