def super_isinstance(super_inst, cls):
    'Is the cls in the mro somewhere after the current class?'
    mro = super_inst.__self__.__class__.__mro__
    thisclass = super_inst.__thisclass__
    return cls in mro and mro.index(thisclass) < mro.index(cls)