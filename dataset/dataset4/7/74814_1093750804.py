elem = match.group(1).lower() # script or style
if self.cdata_elem is not None:
    if elem != self.cdata_elem:
        self.handle_data(rawdata[i:gtpos])
        return gtpos

self.handle_endtag(elem.lower())