def _decode(self, position):  # private helper
    line, col = position.split('.')
    line = int(line)
    col = len(self.data[line]) if col == '0 lineend' else int(col)
    return line, col