pat = compile(12 * r'(\d+)')

ltarget = float(pat.sub(r'\10',line))