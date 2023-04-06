import numpy as np
from scipy import sparse
import decimal
D = decimal.Decimal

Al = sparse.dok_matrix((10, 10), dtype=np.dtype(D))
Al.astype(D)