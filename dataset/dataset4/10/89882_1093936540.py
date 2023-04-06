from subprocess import PIPE, Popen, CREATE_NEW_CONSOLE, run

subProcess = Popen("Python", stdin=PIPE, stdout=PIPE, text=True, universal_newlines=True)