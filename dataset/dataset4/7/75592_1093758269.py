import warnings
warnings.filterwarnings('once')
warnings.onceregistry = None
warnings.warn_explicit(message='foo', category=Warning, filename='bar',
                       lineno=1, registry=None)