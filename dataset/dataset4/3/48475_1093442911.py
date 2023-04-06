import parser
s=parser.suite(
     "from __future__ import unicode_literals; print type('')")
eval(s.compile())