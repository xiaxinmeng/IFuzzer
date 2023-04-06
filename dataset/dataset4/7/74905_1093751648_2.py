print(re.sub(pattern, '\\1',
             '<div><p>foo</p>123456789</div>\n'
             '<div><p>bar</p></div>\n'))