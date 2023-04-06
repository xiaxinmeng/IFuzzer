import io
import configparser

ini = configparser.ConfigParser()
ini.optionxform = lambda x: '(' + x + ')'
ini.read_dict({'section A': {'key 1': 'value 1'}})

inifile = io.StringIO()
ini.write(inifile)
print(inifile.getvalue())