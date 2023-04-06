
class BadRepr:
    def __repr__(self):
        raise Exception('repr_exc')


obj = BadRepr()

__import__('pdb').set_trace()
