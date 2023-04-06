def kill_with_taskkill(proc):
    print('kill child with taskkill /F')
    subprocess.run(['taskkill', '/F', '/pid', '%s' % proc.pid], check=True)

def kill_with_stopprocess(proc):
    print('kill child with powershell stop-process')
    subprocess.run(['powershell', 'stop-process', '%s' % proc.pid], check=True)