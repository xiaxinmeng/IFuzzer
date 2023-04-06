re_exc_line = re.compile (
        # ignore everything before the first match
        r'^.*' +
        # first group (includes second | third)
        r'(?:' +
         # second group "(line) (file)"
         r'(?:' +
          # (text to ignore, line [number])
          r'\([^,]+\s*,\s*line\s+(?P<line1>\d+)\)' +
          # any text ([filename]) any text
          r'.*\((?:(?P<file1>[^)]+))*\).*' +
         # end of second group
         r')' +
        # or
        r'|' +
         # third group "(file) (line)"
         r'(?:' +
          # ([filename])
          r'\((?:(?P<file2>[^)]+))*\)' +
          # any text (text to ignore, line [number]) any text
          r'.*\([^,]+\s*,\s*line\s+(?P<line2>\d+)\).*' +
          # end of third group
         r')' +
        # end of first group
        r')' +
        # any text after it
        r'.*$'
        , re.I
    )