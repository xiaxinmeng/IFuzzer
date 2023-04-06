if os.name in ['nt', 'ce'] and name == util.find_msvcrt():  # TODO: handle the extension
  self._handle = windll.kernel32.GetModuleHandleA(self._name)