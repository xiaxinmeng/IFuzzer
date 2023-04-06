class AbstractCryptoHashFunction(metaclass=_abc.ABCMeta):
    """Common ABC for keyed and non-keyed cryptographic hash functions"""

class CryptoHashFunction(AbstractCryptoHashFunction):
    """Abstract base class for cryptographic hash functions (PEP 247)"""

class KeyedCryptoHashFunction(AbstractCryptoHashFunction):
    """Abstract base class for keyed cryptographic hashs function (PEP 247)"""