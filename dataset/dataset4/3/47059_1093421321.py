key = _winreg.OpenKey( _winreg.HKEY_CURRENT_USER, "PythonTestUnicodeKeys" )

one_byte_key = _winreg.EnumKey( key, 0 )
two_byte_key = _winreg.EnumKey( key, 1 )

_winreg.CloseKey( key )