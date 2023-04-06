# main.py
from io import TextIOWrapper

a = TextIOWrapper(open('main.py','rb'))
for i in a:
    pass
a.close()