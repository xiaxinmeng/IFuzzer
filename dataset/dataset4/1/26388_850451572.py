class CodeType:
     def get_variable_name(self, n:int):
           "Return the names of the nth variable"
     def get_variable_scope(self, n:int):
           "Returns the scope of the nth var (one of LOCAL, ESCAPES, FREE)"
     def get_variable_kind(self, n:int):
           "Return the kind of nth var (one of LOCAL, ARG, VARARG, etc)"