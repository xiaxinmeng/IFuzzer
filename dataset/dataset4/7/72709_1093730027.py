# change 'colour' to 'color' in idlelib.configdialog 3.6
with open('F:/python/dev/36/lib/idlelib/configdialog.py', 'r+') as f:
    code = f.read().replace('Colour', 'Color').replace('colour', 'color')
    f.seek(0); f.truncate()
    f.write(code)