# Hit Ctrl+C before the 3 s timeout, and it will delay 10 s
call('trap "" INT && sleep 10', shell=True, timeout=3)