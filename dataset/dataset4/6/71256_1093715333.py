import webbrowser, os

b = webbrowser.get("firefox")
b.open("https://bugs.python.org/issue26741")
b = None

os.system("ps ax|grep firefox")
input("press ENTER when firefox exited")
os.system("ps ax|grep firefox")