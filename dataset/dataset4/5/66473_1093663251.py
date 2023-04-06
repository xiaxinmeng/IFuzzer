
import webbrowser
import subprocess

webbrowser.open('http://www.example.com', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
