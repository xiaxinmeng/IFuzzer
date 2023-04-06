if sys.platform.startswith('win'):
    import subprocess
else:
    import subprocess32 as subprocess