
# test.py
import configparser

cp = configparser.ConfigParser()
cp.read('test.ini')
for k, v in cp.items('DEFAULT'):
    print(k, v)
