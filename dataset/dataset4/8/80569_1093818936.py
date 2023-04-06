
def exc():
    raise Exception()


try:
    exc()
except Exception:
    import pdb
    pdb.post_mortem()
