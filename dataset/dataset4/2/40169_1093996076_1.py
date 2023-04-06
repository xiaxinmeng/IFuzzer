def characters(self, content):
    self._out.write(escape(content).encode(self._encoding))