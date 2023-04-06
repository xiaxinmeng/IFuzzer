# Whether datetime.strftime can handle a trailing % is platform-dependent,
# so detect whether we're on one of the platforms where this fails ([bpo-35066](https://bugs.python.org/issue35066))
try:
    time.strftime('%')
    skip_trailing_percent_strftime = False
except ValueError:
    skip_trailing_percent_strftime = True