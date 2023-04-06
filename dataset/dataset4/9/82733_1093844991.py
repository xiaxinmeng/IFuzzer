
import sys
import colorama

colorama.init()

_GREEN = colorama.Fore.GREEN
_YELLOW = colorama.Fore.YELLOW
_RESET = colorama.Style.RESET_ALL

print("setting prompt, {}, {}, {}.".format(_GREEN, _YELLOW, _RESET))
sys.ps1 = "{}>>> {}".format(_GREEN, _RESET)
sys.ps2 = "{}... {}".format(_YELLOW, _RESET)
print()
