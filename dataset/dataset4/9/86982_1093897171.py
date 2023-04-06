def split_iter(self: str, sep: str) -> 'Iterator[str]':
    return iter(self.split(sep))