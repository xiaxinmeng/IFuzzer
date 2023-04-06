time.sleep(10)
os.system("taskkill /f /im chrome.exe")
os.system("start test.py")
sys.exit("restarting")