if sys.platform == 'win32':
    def _alias_mbcs(encoding):
        try:
            import _winapi
            ansi_code_page = "cp%s" % _winapi.GetACP()
            if encoding == ansi_code_page:
                import encodings.mbcs
                return encodings.mbcs.getregentry()
        except ImportError:
            # Imports may fail while we are shutting down
            pass

    codecs.register(_alias_mbcs)