# thirdpartymodule.py
import warnings
warnings.warn("{} is deprecated".format(__name__), DeprecationWarning)

# mymodule.py
import thirdpartymodule