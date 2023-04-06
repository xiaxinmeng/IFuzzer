import subprocess, time
def leaktest():
    subp = subprocess.Popen("echo hi; sleep 200; echo bye", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #you can do something here
    subp.terminate()
    #subp.wait() #Fixes the bug
    #time.sleep(0.001) #fixes the bug
    #time.sleep(0.0000001) #doesn't fix the bug
    return True