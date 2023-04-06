def guess_all_extensions(self, type, strict=True):
    type = type.lower()
    extensions = self.types_map_inv[True].get(type, [])
    if not strict:
        for ext in self.types_map_inv[False].get(type, []):
            if ext not in extensions:
                extensions.append(ext)
    return extensions