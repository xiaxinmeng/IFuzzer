from email._header_value_parser import *
import email.policy
tl = TokenList([
    TokenList([
        ValueTerminal('x', 'atext'),
        WhiteSpaceTerminal(' ', 'fws'),
        ValueTerminal('x'*76, 'atext'),
    ]),
    ValueTerminal(',', 'list-separator')
])
tl.fold(policy=email.policy.default)