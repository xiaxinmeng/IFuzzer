from configparser import ConfigParser

config = ConfigParser(allow_no_value=True)
config.optionxform = str
config.add_section('default_settings')
config.set('default_settings', '; comment HERE')

with open('example_case.ini', 'w') as configfile: config.write(configfile)
with open('example_case.ini', 'r') as configfile: print(configfile.read())