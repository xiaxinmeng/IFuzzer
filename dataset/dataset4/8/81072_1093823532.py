import os
import sys
prefix = os.path.split(os.path.abspath(sys.executable))[0]
env = os.environ
env['CONDA_DLL_SEARCH_MODIFICATION_ENABLE'] = '1'
env['CONDA_DEFAULT_ENV'] = 'base'
env['CONDA_PREFIX'] = prefix
env['CONDA_SHLVL'] = '1'
# end of first sitevendor example