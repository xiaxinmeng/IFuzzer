self.Emin = DefaultContext.Emin if Emin is None else Emin
self.Emax = DefaultContext.Emax if Emax is None else Emax
self._ignored_flags = [] if _ignored_flags is None else _ignored_flags