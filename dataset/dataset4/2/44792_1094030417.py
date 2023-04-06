# who wants symbols and a many times larger output file
# should explicitly switch the debug mode on
# otherwise we let dllwrap/ld strip the output file
# (On my machine: 10KB < stripped_file < ??100KB
#   unstripped_file = stripped_file + XXX KB
#  ( XXX=254 for a typical python extension))
if not debug:
    extra_preargs.append("-s")