def get_header(self, header_name, default=None):
    return self.headers.get(
        header_name,
        self.unredirected_hdrs.get(header_name, default))