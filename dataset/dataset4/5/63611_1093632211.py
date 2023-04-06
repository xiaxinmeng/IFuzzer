MISSING_C_DOCSTRINGS = (check_impl_detail() and
                        sys.platform != 'win32' and
                        not sysconfig.get_config_var('WITH_DOC_STRINGS'))

HAVE_DOCSTRINGS = _check_docstrings.__doc__ is not None and not MISSING_C_DOCSTRINGS