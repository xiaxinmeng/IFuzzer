import _winreg
list (
     _winreg.IterValue (
         _winreg.OpenKey (_winreg.HKEY_CURRENT_USER, "Console")
      )
)