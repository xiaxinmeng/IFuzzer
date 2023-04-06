#!/usr/bin/python3
import atexit
import subprocess


def preexec():
    pass


def exit_handler():
    proc = subprocess.Popen(
        ["pwd"],
        preexec_fn=preexec,
    )
    proc.communicate()


if __name__ == "__main__":
    atexit.register(exit_handler)