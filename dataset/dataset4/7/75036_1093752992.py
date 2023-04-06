self.font_bold = tracers.add(BooleanVar(parent), self.var_changed_font)
self.space_num = tracers.add(IntVar(parent), ('main', 'Indent', 'num-spaces'))