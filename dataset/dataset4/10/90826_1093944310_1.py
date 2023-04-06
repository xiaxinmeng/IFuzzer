if sys.platform == 'win32':
    def _alias_mbcs(encoding):
        try:
            import _bootlocale
            if encoding == _bootlocale.getpreferredencoding(False):
                import encodings.mbcs
                return encodings.mbcs.getregentry()
        except ImportError:
            # Imports may fail while we are shutting down
            pass

    codecs.register(_alias_mbcs)