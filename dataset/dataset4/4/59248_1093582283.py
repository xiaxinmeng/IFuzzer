def gdb_has_autoload_safepath():
    # Recent GDBs will only auto-load scripts from certain safe
    # locations, so we will need to turn off this protection.
    # However, if the GDB doesn't have it, then the following
    # command will generate noise on stderr (rhbz#817072):
    cmd = "--eval-command=set auto-load safe-path /"
    p = subprocess.Popen(["gdb", "--batch", cmd],
                         stderr=subprocess.PIPE)
    _, stderr = p.communicate()
    return '"on" or "off" expected.' not in stderr
    
HAS_AUTOLOAD_SAFEPATH = gdb_has_autoload_safepath()