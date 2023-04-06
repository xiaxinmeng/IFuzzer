# before:
obj._extra_state = ExtraState(obj)
# after:
extra_states = WeakKeyDictionary()
extra_states[o] = ExtraState(obj)