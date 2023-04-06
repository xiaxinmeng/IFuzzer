#!/bin/python3
import os, subprocess, time

with open("%s/unbuffered_test.log" % (os.getenv("HOME")), "w") as f:
    with subprocess.Popen(["%s/unbuffered_test.sh" % (os.getenv("HOME"))], stdin=subprocess.PIPE, stdout=f, stderr=f) as p:
        p.stdin.write(bytes("test\n", encoding="utf-8"))
        time.sleep(10)