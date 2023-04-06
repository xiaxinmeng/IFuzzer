import sys
import os
import locale
import encodings
import encodings.aliases

test_locales = [
    'ja_JP.UTF-8',
    'de_DE.SJIS',
    'de_DE.foobar',
    'sr_RS.UTF-8@latin',
    'sr_rs@latin',
    'sr@latin',
    'sr_yu',
    'sr_yu.SJIS@devanagari',
    'sr@foobar',
    'sR@foObar',
    'sR',
]

for test_locale in test_locales:
    print("%(orig)s -> %(norm)s"
          %{'orig': test_locale,
            'norm': locale.normalize(test_locale)}
    )