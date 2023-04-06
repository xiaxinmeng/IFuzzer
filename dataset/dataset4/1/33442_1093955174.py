# the dlopen() function means we might want to use dynload_shlib.o. some
# platforms, such as AIX, have dlopen(), but don't want to use it.
AC_CHECK_FUNCS(dlopen)