if hasattr(os, 'listxattr'):
    def _copyxattr(src, dst, *, follow_symlinks=True):
        try:
            names = os.listxattr(src, follow_symlinks=follow_symlinks)
        except OSError as e:
            if e.errno not in (errno.ENOTSUP, errno.ENODATA):
                raise
            return