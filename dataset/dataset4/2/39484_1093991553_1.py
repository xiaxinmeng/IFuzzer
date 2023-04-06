if sequence == "<MouseWheel>":
    cmd = ('%sif {"[%s %s]" == "break"} break\n'
           %
           (add and '+' or '',
            funcid, self._subst_format_str_workaround))
else:
    cmd = ('%sif {"[%s %s]" == "break"} break\n'
           %
           (add and '+' or '',
            funcid, self._subst_format_str))