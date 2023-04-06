#! /usr/bin/env python3

from email import parser
from email.policy import EmailPolicy
from email._header_value_parser import *
from email import _header_value_parser as parser


# Original header : {'Subject': "La particiation rÃ©alisÃ©e le 2016-01-03 02:30:00+00:00 sur le site Vigiechiro - Point Fixe-800752 vient d'Ãªtre traitÃ©e !"}
_parse_tree = UnstructuredTokenList([
	EncodedWord([
		ValueTerminal('La', 'vtext'), WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('particiation', 'vtext'),
		WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('rÃ©alisÃ©e', 'vtext'), WhiteSpaceTerminal(' ', 'fws'),
		ValueTerminal('le', 'vtext'), WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('2016-01-03', 'vtext'),
		WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('02:30:00+00', 'vtext')
	]),
	EWWhiteSpaceTerminal(' ', 'fws'),
	EncodedWord([
		ValueTerminal(':00', 'vtext'), WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('sur', 'vtext'),
		WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('le', 'vtext'), WhiteSpaceTerminal(' ', 'fws'),
		ValueTerminal('site', 'vtext'), WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('Vigiechiro', 'vtext'),
		WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('-', 'vtext'), WhiteSpaceTerminal(' ', 'fws'),
		ValueTerminal('Point', 'vtext'), WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('Fixe-800752', 'vtext'),
		WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('vient', 'vtext'), WhiteSpaceTerminal(' ', 'fws'),
		ValueTerminal("d'Ãª", 'vtext')
	]),
	EWWhiteSpaceTerminal(' ', 'fws'),
	EncodedWord([
		ValueTerminal('tre', 'vtext'), WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('traitÃ©e', 'vtext'),
		WhiteSpaceTerminal(' ', 'fws'), ValueTerminal('!', 'vtext')
	])
])

policy = EmailPolicy(linesep='\r\n')

header = parser.Header([
    parser.HeaderLabel([
        parser.ValueTerminal('Subject', 'header-name'),
        parser.ValueTerminal(':', 'header-sep')]),
    parser.CFWSList([parser.WhiteSpaceTerminal(' ', 'fws')]),
                     _parse_tree])
# Should crash here
folded = header.fold(policy=policy)
print(folded)
