from main import AtomX

def inheritance_map(candidate):
    print(f'{candidate=} {type(candidate)=} {AtomX=}')
    assert isinstance(candidate, AtomX)