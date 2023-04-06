def fix_subprocess_racecondition():
  """
  !!! PLEASE NOTE THIS SHOULD BE CALLED BEFORE ANY OTHER INITIALIZATION was done to avoid already created links to subprocess or subprocess.gc or gc
  """
  # monkey patching subprocess
  import subprocess
  subprocess.gc.isenabled = lambda: True

  # re-importing gc to have correct isenabled for non-subprocess contexts
  import sys
  del sys.modules['gc']
  import gc