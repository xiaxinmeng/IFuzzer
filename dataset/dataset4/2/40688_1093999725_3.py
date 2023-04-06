if not bp.breakingline:
      #the function is entered for the 1st time
      bp.breakingline=frame.f_lineno
if  bp.breakingline != frame.f_lineno:
       return False 