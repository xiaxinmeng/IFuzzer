import ConfigParser

a = ConfigParser.SafeConfigParser()

# borked
a.add_section('DEFAULT')
a.set('DEFAULT', 'foo', 'bar')

# working
a.add_section('working')
a.set('working', 'foo', 'bar')

b = open('testing', 'w')
a.write(b)
b.close()