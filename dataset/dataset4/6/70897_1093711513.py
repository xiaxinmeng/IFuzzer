
import configparser

cp = configparser.ConfigParser({'foo': 'dog'})
print(cp.defaults())
cp.read('app.ini')
print(cp.defaults())
