d = {}
for mapping in reversed(self.maps):
    d.update(mapping)
return iter(d)