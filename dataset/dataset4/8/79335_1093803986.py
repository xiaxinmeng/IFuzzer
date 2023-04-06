import subprocess

def list2cmdlineHack(seq):
    return " ".join(seq)

subprocess.list2cmdline = list2cmdlineHack