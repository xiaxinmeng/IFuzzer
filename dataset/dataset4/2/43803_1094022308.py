def writeheader(self, headernames = {}):
    """Write a header row"""
    if not headernames:
        headernames = dict(zip(self.fieldnames,
self.fieldnames))
        self.writerow(headernames)