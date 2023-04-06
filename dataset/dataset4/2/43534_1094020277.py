#!/usr/bin/python
import tarfile
import sys
tar = tarfile.open(sys.argv[1], "r")
tar.list()