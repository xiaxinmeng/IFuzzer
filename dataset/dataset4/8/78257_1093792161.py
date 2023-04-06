
class _tri(object):
    infts = '(+/-)inf, (+/-)infty, (+/-)infinity'

    strange_failing = {x+s.replace('(+/-)',''):None for x in ('+','-','') for s in infts.split(', ')}
