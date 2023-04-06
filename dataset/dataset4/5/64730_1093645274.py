# -*- coding: utf-8 -*-
import email.parser
meta = """
Header: ☃
"""
email.parser.Parser().parsestr(meta)