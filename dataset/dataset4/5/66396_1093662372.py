# this keeps compatibility from 2.3 to 2.5
if sys.version < "2.6":
    USER_BASE = None
    HAS_USER_SITE = False
else:
    from site import USER_BASE
    HAS_USER_SITE = True