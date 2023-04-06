# TM_DIRECTORY/sitecustomize.py
import sys
# remove this copy of sitecustomize from import path
if "TM_DIRECTORY" in sys.path:
    sys.path.remove("TM_DIRECTORY")
try:
    import sitecustomize    # get module reference
    if sys.version_info[0] >= 3:
        from imp import reload
    reload(sitecustomize)   # try to import another
                            # using altered path
except ImportError:
    pass                    # no other sitecustomize found
# do TM2 customizations here
# ...