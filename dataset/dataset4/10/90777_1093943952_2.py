
"""
>>> print(static_property)
static value
>>> print(lazy_property)
lazy value
"""

static_property = 'static value'


def __getattr__(name):
    if name != 'lazy_property':
        raise AttributeError(name)
    return 'lazy value'
