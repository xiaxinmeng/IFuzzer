print(re.sub(pattern, '\\1',
             '<div><p>foo</p></div>\n'
             '<div><p>bar</p>123456789</div>\n'))