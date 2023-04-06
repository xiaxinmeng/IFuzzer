# A constant likely larger than the underlying OS pipe buffer size, to
# make writes blocking.
# Windows limit seems to be around 512 B, and many Unix kernels have a
# 64 KiB pipe buffer size or 16 * PAGE_SIZE: take a few megs to be sure.
# (see issue python/cpython#62035 for a discussion of this number).
PIPE_MAX_SIZE = 4 * 1024 * 1024 + 1