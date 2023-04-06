#!/usr/bin/env python
with open('/etc/services') as fd:
    lines = fd.readlines()
lines.append('')
SERVICES = [line.split()[0] for line in lines
                                if (line and not line.startswith('#'))]