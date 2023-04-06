# WORKING example:
registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
wholeKey = winreg.OpenKey(registry, 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon', 0, winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
winreg.SetValue(wholeKey, 'AutoAdminLogon', winreg.REG_SZ, '1')
winreg.CloseKey(wholeKey)


# NON-WORKING example:
registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
wholeKey = winreg.OpenKey(registry, 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon', 0, winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
winreg.SetValue(wholeKey, 'AutoAdminLogon', winreg.REG_SZ, '1')
winreg.CloseKey(wholeKey)