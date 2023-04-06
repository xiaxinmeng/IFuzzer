import subprocess
subprocess.run(['cmd.exe', '/c', 'ping 1.2.3.4 -n 9999'], capture_output=True, timeout=1)