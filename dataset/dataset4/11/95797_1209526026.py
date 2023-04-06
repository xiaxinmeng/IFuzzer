
# change() is called continuously by another thread
_GLOBAL = list('first')
def change():
    global _GLOBAL
    _GLOBAL = list('new')

def caller():
    called(_GLOBAL)

while True:
    caller()
