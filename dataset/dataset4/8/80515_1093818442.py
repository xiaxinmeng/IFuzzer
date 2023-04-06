########## INPUT:
pa = [   
    Path('C:/Program Files'),
    Path('C:/')
]
pb = [
    Path('/one/two/three.exe'),
    Path('/four.exe') 
    ]
print( [a/b for a in pa for b in pb] )