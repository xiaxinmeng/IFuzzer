
if '\n' in line and any(x in line.replace(' ', '').strip('\0').upper()
                        for x in ('\nPORT', '\nEPRT')):
     raise
