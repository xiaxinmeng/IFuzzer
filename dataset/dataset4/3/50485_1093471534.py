def pipepager(text, cmd):
    """Page through text by feeding it to another program."""
    import subprocess
    pipe=subprocess.Popen(cmd,stdin=subprocess.PIPE).stdin
    #pipe = os.popen(cmd, 'w')
    try:
        pipe.write(bytes(text,sys.getdefaultencoding()))
        #pipe.write(text)
        pipe.close()
    except IOError:
        pass # Ignore broken pipes caused by quitting the pager program.