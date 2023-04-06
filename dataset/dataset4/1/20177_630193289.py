
#if !defined(HAVE_GETHOSTBYNAME_R) && !defined(MS_WINDOWS)
# define USE_GETHOSTBYNAME_LOCK
#endif
