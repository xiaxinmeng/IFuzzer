import sys
import winreg

def get_help():
    KEY = rf"Software\Python\PythonCore\{sys.winver}\Help\Main Python Documentation"
    try:
        return winreg.QueryValue(winreg.HKEY_CURRENT_USER, KEY)
    except FileNotFoundError:
        pass
    try:
        return winreg.QueryValue(winreg.HKEY_LOCAL_MACHINE, KEY)
    except FileNotFoundError:
        pass
    return f"https://docs.python.org/{sys.version_info.major}.{sys.version_info.minor}/"