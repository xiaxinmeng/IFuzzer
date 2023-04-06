getint = int
class Scale(Widget):
    def get(self):
        """Get the current value as integer or float."""
        value = self.tk.call(self._w, 'get')
        try:
            return getint(value)
        except ValueError:
            return getdouble(value)
    def set(self, value):
        """Set the value to VALUE."""
        self.tk.call(self._w, 'set', value)