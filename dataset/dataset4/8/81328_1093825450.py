import logging

l = logging.Logger("")
h = logging.StreamHandler()
f = logging.Formatter(fmt="[{filename}:{lineno}] {msg}", style="{")
h.setFormatter(f)
l.addHandler(h)
l.info("Hello")