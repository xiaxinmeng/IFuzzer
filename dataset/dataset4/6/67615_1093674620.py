import sys
import os
if not sys.flags.utf8_mode:
    # Force UTF-8 mode
    argv = sys.orig_argv.copy()
    argv[1:1] = ["-X", "utf8"]
    print(f"Re-execute to force UTF-8 mode! argv={argv}")
    os.execv(argv[0], argv)

print(f"Everybody loves UTF-8! utf8_mode={sys.flags.utf8_mode}")