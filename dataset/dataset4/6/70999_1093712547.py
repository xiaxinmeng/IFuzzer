from configparser import *
parser = ConfigParser( interpolation=ExtendedInterpolation() )
parser.add_section( 'Section' )
parser.set( 'Section', 'first', '${userdef}' )
parser.set( 'Section', 'second', '${first}' )
parser[ 'Section' ].get( 'second', vars={'userdef': 'userval'} )