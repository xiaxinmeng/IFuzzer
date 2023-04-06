if not hasattr(Thread, "_Thread__bootstrap_inner"):
    class SafeThread (Thread):
        def encaps(self):
            try:
                self._Thread__bootstrap_inner()
            except:
                if self.__daemonic and sys_ is None:
                    return
                raise
    setattr(SafeThread, "_Thread__bootstrap_inner",
SafeThread._Thread__bootstrap)
    setattr(SafeThread, "_Thread__bootstrap", SafeThread.encaps)
    threading.Thread = SafeThread