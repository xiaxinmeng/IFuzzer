#!/usr/bin/env python
def make_venv(venvpath):
    import os
    import subprocess
    import sysconfig

    python = os.path.join(sysconfig.get_config_var('BINDIR'), 'python3')
    cmd = [python, '-mvenv', venvpath]
    subprocess.run(cmd)

if __name__ == '__main__':
    import sys
    assert len(sys.argv) == 2
    try:
        rc = make_venv(sys.argv[1])
    except Exception as e:
        print('Failed: %s' % e)
        rc = 1
    sys.exit(rc)