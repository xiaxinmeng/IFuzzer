def keepByValue(self, key=None, value=[]):
    for row in self.flows:
        if not row[key] in value:
            flows.remove(row)