class ProxyLexer(object):

    def __init__(self, underlying):
        self.__underlying = underlying

    def __getattr__(self, attr):
        return getattr(self.__underlying, attr)

def setup(app):
    from sphinx.highlighting import lexers
    if lexers is not None:
        lexers['pycon-literal'] = ProxyLexer(lexers['pycon'])
        lexers['pycon3-literal'] = ProxyLexer(lexers['pycon3'])