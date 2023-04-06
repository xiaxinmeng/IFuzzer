import plistlib

xml = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>FloatExample</key>
<real>100.0</real>
<key>FloatExample2</key>
<real>0.1</real>
</dict>
</plist>
"""

pl = plistlib.loads(str.encode(xml), fmt=plistlib.FMT_XML)
with open('test.plist', 'wb') as fp:
  plistlib.dump(pl, fp, fmt=plistlib.FMT_BINARY)