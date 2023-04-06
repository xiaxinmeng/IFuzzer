def find_earliest_header_offset(zf):
    earliest_offset = None
    for zinfo in zf.infolist():
        if earliest_offset is None:
            earliest_offset = zinfo.header_offset
        else:
            earliest_offset = min(zinfo.header_offset, earliest_offset)
    return earliest_offset