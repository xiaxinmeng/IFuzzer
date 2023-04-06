# cache for by mkpath() -- in addition to cheapening redundant calls,
# eliminates redundant "creating /foo/bar/baz" messages in dry-run mode
_path_created = set()