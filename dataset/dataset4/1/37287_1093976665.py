if not srcDir:
    raise EnvironmentError("The system configuration"
        " variable 'srcdir' is not defined, so this"
        " setup script cannot continue.  This error"
        " probably arose because this setup script"
        " is only designed to run in the Cygwin"
        " environment, yet you are attempting to"
        " run it elsewhere."
      )
##################################################