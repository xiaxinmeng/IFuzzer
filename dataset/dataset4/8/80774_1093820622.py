# Workaround for issue python/cpython#56579
# Without this, the __class__ properties wouldn't be set correctly
_safe_super = super