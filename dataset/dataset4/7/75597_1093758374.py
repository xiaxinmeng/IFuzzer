import warnings
warnings.filters = [(None, None, Warning, None, 0)]
warnings.warn_explicit(message='foo', category=Warning, filename='bar',
                       lineno=1)