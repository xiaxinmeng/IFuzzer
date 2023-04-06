
import subprocess
  
def is_apfs(path):
    lines = subprocess.check_output(['df', path]).decode('utf-8').splitlines()
    mountpoint = lines[1].split(None, 1)[0]

    lines = subprocess.check_output(['mount']).decode('utf-8').splitlines()
    for ln in lines:
        path = ln.split(None, 1)[0]
        if path == mountpoint:
            return '(apfs' in ln

    return False
