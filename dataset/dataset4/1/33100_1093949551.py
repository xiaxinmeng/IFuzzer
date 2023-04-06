def wm_resizable(self, width=None, height=None):
       return self._getints(
                        self.tk.call('wm', 'resizable',                                 self._w, width, height))