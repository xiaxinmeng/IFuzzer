import numpy as np

from unittest import mock as mg

ob = mg.Mock(spec=[4, 4])
print("spec is list, mock is", ob)

ob = mg.Mock(spec=["4", "4"])
print("spec is list of str, mock is", ob)

ob = mg.Mock(spec=(4, 4))
print("spec is tuple, mock is", ob)

ob = mg.Mock(spec="cow")
print("spec is string, mock is", ob)

ob = mg.Mock(spec=22)
print("spec is int, mock is", ob)

ob = mg.Mock(spec=np.array([4, 4]))
print("spec is ndarray, mock is", ob)