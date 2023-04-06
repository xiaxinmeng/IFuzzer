if ENV_PYTHONEXECUTABLE or ENV___PYVENV_LAUNCHER__:
     # If set, these variables imply that we should be using them as
     # sys.executable and when searching for venvs. However, we should
     # use the argv0 path for prefix calculation
     if os_name != 'darwin':
         base_executable = executable
     if not real_executable:
         real_executable = executable
     executable = ENV_PYTHONEXECUTABLE or ENV___PYVENV_LAUNCHER__
     executable_dir = dirname(executable)