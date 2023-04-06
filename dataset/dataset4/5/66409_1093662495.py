import sys
sys.executable = r"Path to the python executable inside the venv"
path = sys.path
for i in range(len(path)-1, -1, -1):
    if path[i].find("site-packages") > 0:
        path.pop(i)
import site
site.main()
del sys, path, i, site