def pformat(self, _indent_level=1):
    out = '{0.__module__}.{0.__qualname__}'.format(self.cls)

    for child in self.children:
        out += '\n' + '\t' * _indent_level + child.pformat(_indent_level+1)

    return out