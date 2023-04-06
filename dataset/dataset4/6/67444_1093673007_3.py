resolved_path = self._resolve_path(path)
if path != resolved_path:
    self.redirect(resolved_path)