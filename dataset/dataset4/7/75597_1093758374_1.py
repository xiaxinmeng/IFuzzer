import warnings
warnings.defaultaction = None
warnings.filters = []
warnings.warn_explicit(message='foo', category=Warning, filename='bar',
                       lineno=1)