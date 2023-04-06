template = b"""
stuff here
header1: {}
header2: {}
more stuff
"""

def lowlevel_send(s, b1, b2):  # s socket, b1 and b2 bytes
    s.send(template.format(b1, b2))